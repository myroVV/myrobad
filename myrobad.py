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
    if message.channel.id == 756327903679217695:
        await message.add_reaction("😱")

@client.event
async def on_message(message):
    if message.content.startswith('{bot.user.mention}'):
        await bot.send_message(message.channel, f"Don't tag me, please go fuck yourself.")

client.run(os.environ['DISCORD_TOKEN'])
