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
        userembed.add_field(name="  **Usage - You are missing missions permissions to ban users**", value="`:(`", inline=False)
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
        userembed.add_field(name="  **Usage - You are missing missions permissions to kick users**", value="`:(`", inline=False)
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
        userembed.add_field(name="  **Usage - You are missing missions permissions to purge messages**", value="`:(`", inline=False)
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




@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.guild)
async def pp(ctx, member: discord.Member):
    sizes = ['8D',
                '8=D 1 inch LOL!📏',
                '8==D 2 inches KEKW 📏',
                '8==D 2 inches KEKW 📏',
                '8==D 2 inches KEKW 📏',
                '8==D 2 inches KEKW 📏',
                '8===D 3 inches D: 📏',
                '8===D 3 inches D: 📏',
                '8===D 3 inches D: 📏',
                '8===D 3 inches D: 📏',
                '8===D 3 inches D: 📏',
                '8====D 4 inches, ay bruh u good? 📏',
                '8====D 4 inches, ay bruh u good? 📏',  
                '8====D 4 inches, ay bruh u good? 📏',  
                '8====D 4 inches, ay bruh u good? 📏',  
                '8=====D 5 inches :O 📏',
                '8=====D 5 inches :O 📏',
                '8=====D 5 inches :O 📏',
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8======D 6 inches 🤷‍♂️', 
                '8=======D 7 inches 📏',
                '8=======D 7 inches 📏',
                '8=======D 7 inches 📏',
                '8=======D 7 inches 📏',
                '8=======D 7 inches 📏',
                '8========D 8 inches 📏',
                '8========D 8 inches 📏',
                '8========D 8 inches 📏',
                '8========D 8 inches 📏',
                '8=========D 9 inches 📏',
                '8==========D 10 inches 📏',
                '8===========D 11 inches 📏',
                '8============D 12 inches 📏',
                '8=============D 13 inches 📏',
                '8==============D 14 inches 📏',
                '8===============D 15 inches 📏',
                '8================D 16 inches 📏',
                '8=================D 17 inches 📏',
                '8==================D 18 inches 📏',
                '8===================D 19 inches 📏',
                '8==============================D 30 inches 😵',
                '8===============================D 31 inches 😵😵',
                '8========================================D 40 inches!??!?!?!?! 😵😵']
    await ctx.send(f"{member.mention} : ``{random.choice(sizes)}``")


@pp.error
async def dicksize_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**PP CALCULATOR 3900**__", color=0xffffff)
                userembed.add_field(name="  ``Usage - .pp <user>``", value="`🍆🍆🍆🍆`", inline=False)
                await ctx.send(embed=userembed)



@pp.error
async def pp_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error




@client.command(aliases=['8ball'])
@commands.cooldown(1, 3, commands.BucketType.guild)
async def _8ball(ctx, *, question):
    responces = ['Yes',
                 'Yessir',
                 'Squirt first 😳',
                 'Naw',
                 'Maybe',
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


@commands.command()
async def fact(ctx, self):
        url = f'https://uselessfacts.jsph.pl/random.json?language=en'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r['text']
                embed = discord.Embed(title=f'Random Fact', colour=ctx.author.colour, timestamp=ctx.message.created_at)

                embed.add_field(name='***Fun Fact***', value=fact, inline=False)
                await ctx.send(embed=embed)




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
    embed.add_field(name="._8ball (Question)", value=f"8ball O_O.", inline=False)
    embed.add_field(name=".pp (User)", value=f"Find out how long your peepee is!", inline=False)
    embed.add_field(name=".coinflip, .cf", value=f"flips a coin!", inline=False)
    embed.add_field(name=".Ban", value=f"Bans a user.", inline=False)
    embed.add_field(name=".Unban", value=f"Unbans a user.", inline=False)
    embed.add_field(name=".Kick", value=f"Kicks a user.", inline=False)
    embed.add_field(name=".userinfo (User)", value=f"Shows the info of the given user.", inline=False)
    embed.add_field(name=".Covid (Country/Continent) (Name)", value=f"Shows the COVID statistics.", inline=False)
    embed.add_field(name=".Ping", value=f"Gets the latency of the bot.", inline=False)
    embed.set_footer(text=f"Suggested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)










client.run(os.environ['DISCORD_TOKEN'])