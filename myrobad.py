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
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def ping(ctx):
    await ctx.send('Pong')



@client.command()
@commands.has_permission(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'``Member {member} has been kicked.``')


@client.command()
@commands.has_permission(ban_members=True)
async def ban(ctx, self, anything: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'``Member {member} has been banned.``')



client.run(os.environ['DISCORD_TOKEN'])