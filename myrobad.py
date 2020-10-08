# Standard libraries
import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="WRLD On Drugs"))
    print('Bot is online')



client.run(os.environ['DISCORD_TOKEN'])
