import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="myro the best", type = 3))
    print('On')

client.run(os.environ['DISCORD_TOKEN'])