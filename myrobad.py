import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="O_O"))
    print('Bot is online')


client.run(os.environ['DISCORD_TOKEN'])