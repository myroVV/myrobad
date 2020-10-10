import discord
import os
import random
from discord.ext import commands


client = discord.Client()

client = commands.Bot(command_prefix="=")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Whole Lotta Red"))
    print('Bot is online')


@client.command()
async def coinflip(ctx):
    choices = ["``Heads``", "``Tails``"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def kick(ctx, discord.member=None):
    if not member:
        await ctx.send("``Please specify a user``")
        return
    await member.kick()
    await ctx.send(f"``{member.mention} has been kicked.``")



@client.command()
async def ban(ctx, discord.member=None):
    if not member:
        await ctx.send("``Please specify a user``")
        return
    await member.ban()
    await ctx.send(f"``{member.mention} has been banned.``")





client.run(os.environ['DISCORD_TOKEN'])