import discord
import os
from discord.ext import commands


@bot.event
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



@bot.event
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
