import threading
import urllib.request

from discord.ext import commands

from main import ist_admin # Scheint zu funktionieren.

class Update(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.update_lock = threading.Lock()
        self.updatebare_cogs = dict()

        t = self.updatebare_cogs

        t["ehre"] = "https://raw.githubusercontent.com/chamaedoreapruductions/Ehrenhaftrer-Discord-Bot/main/cogs/ehre.py"
        t["lilgadgets"] = "https://raw.githubusercontent.com/chamaedoreapruductions/Ehrenhaftrer-Discord-Bot/main/cogs/lilgadgets.py"
        t["update"] = "https://raw.githubusercontent.com/chamaedoreapruductions/Ehrenhaftrer-Discord-Bot/main/cogs/update.py"
        
        del t

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Cogs are working (update.py)')

    @commands.command()
    @commands.check(ist_admin)
    async def update(self, ctx, cog:str):
        with self.update_lock:
            if cog in self.updatebare_cogs:
                url = self.updatebare_cogs[cog]

                x = urllib.request.urlopen(url).read().decode("utf-8")
                
                with open(f"cogs/{cog}.py", "w", newline='') as d:
                    d.write(x)

                await ctx.send(f"Cog {cog} wurde geupdatet, 'reload {cog}' um die Änderungen gültig zu machen.")

            else:
                await ctx.send(f"Cog {cog} ist nicht in der Update-Liste.")

def setup(client):
    client.add_cog(Update(client))
