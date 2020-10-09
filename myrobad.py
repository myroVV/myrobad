import discord
import os

client = discord.Client()

@client.event
async def on_ready():
<<<<<<< HEAD
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Whole Lotta Red"))
=======
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="WRLD On Drugs"))
    print('Bot is online')
>>>>>>> parent of 9c645e4... Update myrobad.py

client.run(os.environ['DISCORD_TOKEN'])