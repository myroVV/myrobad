import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print('Bot is ready.')


client.run(os.environ['DISCORD_TOKEN'])