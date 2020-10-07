# Standard libraries
import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('999'))
    print('Bot is online')

@client.event
async def on_message(message):

     if "no one asked" in message.content:
           await Bot.send_message(message.channel, 'I asked wdym u mean')

           


client.run(os.environ['DISCORD_TOKEN'])
