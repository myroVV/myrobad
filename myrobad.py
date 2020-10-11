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
@commands.has_permissions(administrator=True) #this line checks if the user who uses the kick command has permission to kick a member from the server
async def kick(ctx, member : discord.Member, *, reason=None):  #here as usual we use the ctx and member: discord.Member is used for mentioning some user and storing it
    await member.kick(reason=reason)  #now , this statement performs the actions ie. kicking the user from the server 
    await ctx.send(f"{member.mention} **has been kicked for** ``{reason}``") #and at last here we display the person who was kicked and the reason he was kicked for


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} **has been banned for** ``{reason}``")
            


@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        userembed=discord.Embed(title="__**Missing Permissions**__", color=0xffffff)
        userembed.add_field(name="  **You are missing missions permissions to ban users**", value="`:(`", inline=False)
        await ctx.send(embed=userembed)

    if isinstance(error, commands.MissingRequiredArgument):
        userembed=discord.Embed(title="__**Ban**__", color=0xffffff)
        userembed.add_field(name="  **Usage - .ban (User)**", value="*Bans a user*", inline=False)
        await ctx.send(embed=userembed)

    else:
        raise(error)

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        userembed=discord.Embed(title="__**Missing Permissions**__", color=0xffffff)
        userembed.add_field(name="  **You are missing missions permissions to kick users**", value="`:(`", inline=False)
        await ctx.send(embed=userembed)

    if isinstance(error, commands.MissingRequiredArgument):
        userembed=discord.Embed(title="__**Ban**__", color=0xffffff)
        userembed.add_field(name="  **Usage - .Kick (User)**", value="*Kicks a user*", inline=False)
        await ctx.send(embed=userembed)

    else:
        raise(error)


@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        userembed=discord.Embed(title="__**Missing Permissions**__", color=0xffffff)
        userembed.add_field(name="  **You are missing missions permissions to purge messages**", value="`:(`", inline=False)
        await ctx.send(embed=userembed)

    if isinstance(error, commands.MissingRequiredArgument):
        userembed=discord.Embed(title="__**Ban**__", color=0xffffff)
        userembed.add_field(name="  **Usage - .clear (x)**", value="*Purges chat by the given amount*", inline=False)
        await ctx.send(embed=userembed)

    else:
        raise(error)





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



@client.command(description="Unbans a member")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} **has been unbanned.**")
            return







@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"``Unmuted`` {member.mention}")
    await member.send(f"``You were unmuted in the server`` {ctx.guild.name}")



@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="More commands coming soon!", color=0x6da860, timestamp=datetime.utcnow())
    embed.add_field(name="**Mod**", value=f"``.kick`` ``.ban`` ``.mute`` ``.lock``", inline=False)
    embed.add_field(name="**Fun**", value=f"``.8ball`` ``.iq`` ``.ego`` ``.pp`` ``.potacc`` ``.potaccuracy`` ``.hack`` ``.slot`` ``.fact``", inline=False)
    embed.add_field(name="**Info**", value=f"``.av`` ``.avatar`` ``.userinfo``", inline=False)
    embed.add_field(name="**Mod**", value=f"``.kick`` ``.ban`` ``.mute`` ``.lock`` ``.covid`` ``.news`` ", inline=False)
    embed.set_footer(text=f"Suggested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)




client.run(os.environ['DISCORD_TOKEN'])