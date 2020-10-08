# Standard libraries
import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('𝟗 𝟗 𝟗'))
    print('Bot is online')

client.run(os.environ['DISCORD_TOKEN'])
