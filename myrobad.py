import discord
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print ('Online')

@client.event
async def on_message(message):
    if message.channel.id == 698639022125219903:
        await message.channel.send("no one asked")


@bot.event
async def on_message(message):
    #Ignore messages sent by yourself
    if message.author.id == bot.user.id:
        return


    

client.run(os.environ['DISCORD_TOKEN'])