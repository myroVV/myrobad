import discord
import os

client = discord.client()

@client.event
async def on_ready():
    print('On')

client.run(os.environ['DISCORD_TOKEN'])