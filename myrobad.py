import discord
import os
import random
from time import sleep
import time
from discord import Spotify
from pathlib import Path
import asyncio
from aiohttp import ClientSession
import aiohttp
from discord.ext import commands, tasks
from random import choice
from discord.voice_client import VoiceClient
from datetime import datetime
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown


client = discord.Client()

client = commands.Bot(command_prefix=".")
client.remove_command("help")



@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Whole Lotta Red"))
    print('Bot is online')


@client.command()
async def coinflip(ctx):
    choices = ["``Heads``", "``Tails``"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


@client.command(aliases=['cl'])
async def clear(ctx, amount=7):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = f"{member.name}'s avatar", color = member.color , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by : {ctx.author}",icon_url=ctx.author.avatar_url)  
    await ctx.send(embed=embed)







@client.command()
async def members(ctx):
    await ctx.send("``Membercount : {0.member_count}``".format(ctx.message.guild))





@client.command(pass_context=True)
async def hack(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("``Please specify a user!``")
        return

    passwords=['dousquirt','sendnoodes63','ilovenood-','myrotrashcoder','unblacklistmyro','hackedlol','quickied','insta2dpce','kookikooki','69'] 
    fakeips=['154.2345.24.743','255.255. 255.0','356.653.56','101.12.8.6053','255.255. 255.0']

    embed=discord.Embed(title=f"**Hacking: {member}** 0%", color=0x2f3136)
    m = await ctx.send(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 19%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 34%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 55%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 67%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 84%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 99%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 100%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(3)
    embed=discord.Embed(title=f"{member}'s info ", description=f"**Email: `{member}@hacked.com` Password: `{random.choice(passwords)}`  IP: `{random.choice(fakeips)}`**", color=0x2f3136)
    embed.set_footer(text="Sending Insta 2s to your house! 😈")
    await m.edit(embed=embed)
    time.sleep(1)






@client.command(aliases=['8ball'])
@commands.cooldown(1, 3, commands.BucketType.guild)
async def _8ball(ctx, *, question):
    responces = ['Yes',
                 'Yessir',
                 'Squirt first 😳',
                 'Naw',
                 'Maybe',
                 'Idk bro you ask me',
                 'Ur mom lol',
                 'Stfu dumb retard',
                 'Dude no lol',
                 'No way Jose',
                 'DA VINKI?',
                 'Not at all bro']
    await ctx.send(f'``Question:`` **{question}**\n``Answer``: **{random.choice(responces)}**')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error




@client.command()
async def boop (ctx, member:discord.User=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("``You cannot boop yourself``")
        return
    await ctx.channel.send(f"``✅ {member} Has been successfully booped! ✅``")

  




@client.command(description="Bot's latency.")
async def ping(ctx):
    latency = round(client.latency * 1000, 1)
    await ctx.send(f"``Pong! {latency}ms``")




@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="More commands coming soon!", color=0x6da860, timestamp=datetime.utcnow())
    embed.add_field(name="**Mod**", value=f"``.kick`` ``.ban`` ``.mute`` ``.lock``", inline=False)
    embed.add_field(name="**Fun**", value=f"``.8ball`` ``.iq`` ``.ego`` ``.pp`` ``.potacc`` ``.potaccuracy`` ``.hack`` ``.slot`` ``.fact`` ``.gay`` ", inline=False)
    embed.add_field(name="**Info**", value=f"``.av`` ``.avatar`` ``.userinfo`` ``.covid`` ``.news``", inline=False)
    embed.set_footer(text=f"Suggested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)













client.run(os.environ['DISCORD_TOKEN'])