# Standard libraries
import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('myro > all'))
    print('Bot is online')

@client.event
async def on_message(message):
    if bot.user.mentioned_in(message) and 'prefix' in message.content:
        await bot.send_message(message.channel, f'I do not have a prefix, stop tagging me you stupid bitch <o/')


client.run(os.environ['DISCORD_TOKEN'])
