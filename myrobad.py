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

@client.event
async def on_message(message):
    if message.channel.id == 698639022125219903:
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')
        await message.add_reaction('🟡')
        await message.add_reaction('🟢')
        await message.add_reaction('🔵')
        await message.add_reaction('🟣')

client.run(os.environ['DISCORD_TOKEN'])