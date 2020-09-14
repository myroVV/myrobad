import discord
import os
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_message(message):
    if(message.channel.id == "698639022125219903"):
        await bot.add_reaction(message, ":thinking:")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print('Bot is ready.')


client.run(os.environ['DISCORD_TOKEN'])