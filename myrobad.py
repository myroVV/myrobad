import discord
import os
from discord.ext import commands
import asyncio

client = discord.Client()

bot = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print ('Online')


@client.event
async def on_message(message):
    if message.author.id == 701974976911245382:
        return

@bot.command()
async def echo(*args):
    output = " "
    for word in args:
        output += word
        output += " "
    await bot.say(output)

client.run(os.environ['DISCORD_TOKEN'])