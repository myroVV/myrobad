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
        await message.add_reaction("😀")
        await message.add_reaction("😄")
        await message.add_reaction("😁")
        await message.add_reaction("😆")
        await message.add_reaction("😌")
        await message.add_reaction("🤓")
        await message.add_reaction("😥")
        await message.add_reaction("👺")
        await message.add_reaction("🤡")
        await message.add_reaction("😿")
        await message.add_reaction("🤢")
        await message.add_reaction("🤖")
        await message.add_reaction("👾")
        await message.add_reaction("😎")
        await message.add_reaction("☠️")
        await message.add_reaction("🤑")



@client.event
async def on_message(message):
    if message.channel.id == 738971995068170240:
        await message.add_reaction("😀")
        await message.add_reaction("😄")
        await message.add_reaction("😁")
        await message.add_reaction("😆")
        await message.add_reaction("😌")
        await message.add_reaction("🤓")
        await message.add_reaction("😥")
        await message.add_reaction("👺")
        await message.add_reaction("🤡")
        await message.add_reaction("😿")
        await message.add_reaction("🤢")
        await message.add_reaction("🤖")
        await message.add_reaction("👾")
        await message.add_reaction("😎")
        await message.add_reaction("☠️")
        await message.add_reaction("🤑")


@client.event
async def on_message():
    if message.channel.id == 728810273653260338:
        await message.add_reaction("🤡")








#-------------------------- Destroyer ----------------------------#

@client.event
async def on_message(message):
    if message.content.lower().strip() == 'no one asked':
        general_channel = client.get_channel(698639022125219903)
        await general_channel.send('I asked')

@client.event
async def on_message(message):
    if message.content.lower().strip() == 'no one asked':
        general_channel = client.get_channel(738971995068170240)
        await general_channel.send('I asked')
    

@client.event
async def on_message(message):
    if message.content.lower().strip() == 'no one cares':
        general_channel = client.get_channel(698639022125219903)
        await general_channel.send('I care')


@client.event
async def on_message(message):
    if message.content.lower().strip() == 'no one cares':
        general_channel = client.get_channel(738971995068170240)
        await general_channel.send('I care')


client.run(os.environ['DISCORD_TOKEN'])
