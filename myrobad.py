import discord
import os

client = discord.Client()


# --------------- STATUS -------------------#
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="myro the best")
    print('On')
# -------------------------------------------#


client.run(os.environ['DISCORD_TOKEN'])