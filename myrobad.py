import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print('myrosaurus is ready.')


@client.event
async def on_message(message):
    if message.channel.id == 698639022125219903:
        await message.add_reaction("😱")





client.run(os.environ['DISCORD_TOKEN'])