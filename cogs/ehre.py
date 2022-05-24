import threading
import json

import discord
from discord.ext import commands

from main import ist_admin # Scheint zu funktionieren.

class Ehre(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.lock = threading.Lock()
        self.ehre_dict = dict()

        with open("data/amount.json", "r") as d:
            self.nexter_save_name = json.loads(d.read())

        if self.nexter_save_name > 0:
            with open(f"data/{self.nexter_save_name - 1}.json", "r") as d:
                daten = json.loads(d.read())

            for i in range(0, len(daten), 1):
                self.ehre_dict[daten[i][0]] = daten[i][1]

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Cogs are working (ehre.py)')

    @commands.command()
    async def ehre(self, ctx, nutzer: discord.Member, ehre: int):
        neu = False
        nutzer = nutzer.id

        with self.lock:
            if nutzer in self.ehre_dict:
                self.ehre_dict[nutzer] += ehre
            else:
                self.ehre_dict[nutzer] = ehre
                neu = True

            ehre = self.ehre_dict[nutzer]

        if neu:
            await ctx.send(f"Nutzer <@{nutzer}> nimmt jetzt teil und hat jetzt Ehre {ehre}")
        else:
            await ctx.send(f"Nutzer <@{nutzer}> hat jetzt Ehre {ehre}")

    @commands.command()
    @commands.check(ist_admin)
    async def alle_ehre(self, ctx):
        inhalt = ""

        for i in self.ehre_dict:
            inhalt += "<@"
            inhalt += str(i)
            inhalt += ">"
            inhalt += " "
            inhalt += str(self.ehre_dict[i])
            inhalt += "\n"

        if inhalt == "":
            await ctx.send("Hier ist es Ehrenlos.")
        else:
            await ctx.send(inhalt)

    @commands.command()
    async def ehre_for_ever(self, ctx):
        zum_speichern = list()

        with self.lock:
            for i in self.ehre_dict:
                zum_speichern.append([i, self.ehre_dict[i]])

            if zum_speichern == []:
                await ctx.send("Hier ist es Ehrenlos.")
                return
            else:
                with open(f"data/{self.nexter_save_name}.json", "w") as d:
                    d.write(json.dumps(zum_speichern))

                self.nexter_save_name += 1

                with open("data/amount.json", "w") as d:
                    d.write(json.dumps(self.nexter_save_name))

                await ctx.send("Gespeichert!")

def setup(client):
    client.add_cog(Ehre(client))
