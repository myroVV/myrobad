import discord
import os
import random
from discord.ext import commands


client = discord.Client()

client = commands.Bot(command_prefix="=")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Whole Lotta Red"))
    print('Bot is online')


@client.command()
async def coinflip(ctx):
    choices = ["``Heads``", "``Tails``"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)



client.run(os.environ['DISCORD_TOKEN'])