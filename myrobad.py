# Standard libraries
import os
import logging

# Third party libraries
import discord
from discord.ext import commands


@client.event
async def on_message(message):
    if message.channel.id == 698639022125219903:
        await message.add_reaction("😀")
        await message.add_reaction("😃")
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
        await message.add_reaction("😃")
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

    

    client.run(os.environ['DISCORD_TOKEN'])
