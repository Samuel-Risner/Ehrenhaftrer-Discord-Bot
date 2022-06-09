import threading
import json

import discord
from discord.ext import commands

from main import ist_admin

class Ehre(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.ehre_lock = threading.Lock()
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
        nutzer = nutzer.id
        sender = ctx.author.id

        with self.ehre_lock:
            if sender in self.ehre_dict:
                if nutzer == sender:
                    await ctx.send(f"Nutzer <@{nutzer}> hat versucht sich selber Ehre zu geben.")
                elif nutzer in self.ehre_dict:
                    self.ehre_dict[nutzer] += ehre
                    await ctx.send(f"Nutzer <@{nutzer}> hat jetzt Ehre {self.ehre_dict[nutzer]}")
                else:
                    await ctx.send(f"Nutzer <@{nutzer}> nimmt nicht teil.")
            else:
                await ctx.send(f"Du musst teilnehmen um mitzumachen <@{nutzer}>")

    @commands.command()
    async def neuer_ehren_kampfhelikopter(self, ctx, nutzer: discord.Member):
        nutzer = nutzer.id

        with self.ehre_lock:
            if nutzer in self.ehre_dict:
                await ctx.send(f"Nutzer <@{nutzer}> nimmt bereits teil.")
            else:
                self.ehre_dict[nutzer] = 0
                await ctx.send(f"Nutzer <@{nutzer}> nimmt jetzt teil.")

    @commands.command()
    async def alle_ehre(self, ctx):
        inhalt = ""

        with self.ehre_lock:
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

    @commands.command(hidden=True)
    @commands.check(ist_admin)
    async def ehre_for_ever(self, ctx):
        zum_speichern = list()

        with self.ehre_lock:
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
