import discord
import os
from discord.ext import commands

client = discord.Client()

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
    if message.channel.content == 'no one asked':
        await message.channel.send('I asked')


client.run(os.environ['DISCORD_TOKEN'])