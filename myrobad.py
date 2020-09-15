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
    if message.channel.id == 698639022125219903:
        await message.channel.send("no one asked")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot: return
    if message.content.startswith('no one asked'):
        msg = 'no one asked'.format(message)
        await client.send_message(message.channel, msg)


    

client.run(os.environ['DISCORD_TOKEN'])