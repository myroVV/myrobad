import discord
import os
import random
from discord.ext import commands


client = discord.Client()

client = commands.Bot(command_prefix=".")


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
async def clear(ctx, amount=7):
    await ctx.channel.purge(limit=amount)


@client.command(name='avatar', aliases=['Avatar, 'av'])
async def av_cmd(ctx, user: discord.Member):
   mbed = discord.Embed(
       color = discord.Color(0xffff),
       title=f"{user}"
   )
    mbed.set_image(url=f"{user.avatar_url}")
    await ctx.send(embed=mbed)




client.run(os.environ['DISCORD_TOKEN'])