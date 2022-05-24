import threading
import discord
from discord.ext import commands
import json

from main import ist_admin

class Update(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.update_lock = threading.Lock()
        self.updatebare_cogs = dict()

        t = self.updatebare_cogs

        t["ehre"] = ""
        t["lilgadgets"] = ""
        t["update"] = ""
        del t

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Cogs are working (update.py)')

    @commands.command()
    @commands.check(ist_admin)
    async def update(self, ctx, cog):
        with self.update_lock:
            if cog in self.updatebare_cogs:
                pass

def setup(client):
    client.add_cog(Update(client))
