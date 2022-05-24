import discord
from discord.ext import commands, tasks
import os
from itertools import cycle

with open("Einstellungen/TOKEN.txt", "r") as d:
    TOKEN = d.read()

with open("Einstellungen/admins.txt", "r") as d:
    admins = d.read()

admins = admins.split("\n")

for i in range(0, len(admins), 1):
    admins[i] = int(admins[i])

with open("Einstellungen/command_prefix.txt", "r") as d:
    COMMAND_PREFIX = d.read()

with open("Einstellungen/status_liste.txt", "r") as d:
    status_liste = d.read()

status_liste = status_liste.split("\n")

client = commands.Bot(command_prefix = COMMAND_PREFIX)

status = cycle(status_liste)

@commands.command()
async def ist_admin(ctx):
    print(__name__)
    return ctx.author.id in admins

@client.command()
@commands.check(ist_admin)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'loaded {extension}')
    await ctx.send(f'loaded {extension}')

@client.command()
@commands.check(ist_admin)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'unloaded {extension}')
    await ctx.send(f'unloaded {extension}')

@client.command()
@commands.check(ist_admin)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'reloaded {extension}')
    await ctx.send(f'reloaded {extension}')

@client.event
async def on_ready():
    change_status.start()
    print("We have logged in as {0.user}".format(client))

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
