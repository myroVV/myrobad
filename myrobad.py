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

@client.command()
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
        await ctx.send(f'{ctx.author.mention} ``You do not have the permission to ban someone!``')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} ``Please specify a user!``")

    else:
        raise(error)


@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} ``You do not have the permission to kick someone!``')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} ``Please specify a user!``")

    else:
        raise(error)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("``You don't have permission to access this command!``")  




@client.command()
async def members(ctx):
    await ctx.send("``Membercount : {0.member_count}``".format(ctx.message.guild))





@client.command(pass_context=True)
async def hack(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("``Please specify a user!``")
        return

    passwords=['imnothackedlmao','sendnoodles63','ilovenoodles','icantcode','christianmicraft','server','icantspell','hackedlmao','WOWTONIGHT','69'] 
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
async def pp(ctx, member: discord.Member):
    sizes = ['8D',
                '8=D **1 inch LOL!📏**',
                '8==D **2 inches KEKW 📏**',
                '8===D **3 inches D: 📏**',
                '8====D **4 inches, ay bruh u good? 📏**',  
                '8=====D **5 inches :O 📏**',
                '8======D **6 inches 🤷‍♂️**', 
                '8=======D **7 inches 📏',
                '8========D **8 inches 📏**',
                '8=========D **9 inches 📏**',
                '8==========D **10 inches 📏**',
                '8===========D **11 inches 📏**',
                '8============D **12 inches 📏**',
                '8=============D **13 inches 📏**',
                '8==============D **14 inches 📏**',
                '8===============D **15 inches 📏**',
                '8================D **16 inches 📏**',
                '8=================D **17 inches 📏**',
                '8==================D **18 inches 📏**',
                '8===================D **19 inches 📏**',
                '8==============================D **30 inches 😵**',
                '8===============================D **31 inches 😵😵**',
                '8========================================D **40 inches!??!?!?!?! 😵😵**']
    await ctx.send(f"{member.mention}'s pp = {random.choice(sizes)}")

@pp.error
async def dicksize_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                userembed=discord.Embed(title="__**PP CALCULATOR 3900**__", color=0xffffff)
                userembed.add_field(name="  ``Usage - .pp <user>``", value="`🍆🍆🍆🍆`", inline=False)
                await ctx.send(embed=userembed)






@client.command()
async def userinfo (ctx):

    list = ''
    for role in ctx.author.roles:
        list += f'<@&{role.id}> '

    embed = discord.Embed(title=f'{ctx.author.name}', description=f"User info of {ctx.author.name}", colour=ctx.author.colour)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name='Tag#:', value=ctx.author, inline=True)
    embed.add_field(name='Nick:', value=ctx.author.nick, inline=True)
    embed.add_field(name='Status:', value=ctx.author.status,inline=True )
    embed.add_field(name='ID:', value=ctx.author.id, inline=False)
    embed.add_field(name='Created:', value=ctx.author.created_at, inline=False)
    embed.add_field(name='Joined:', value=ctx.author.joined_at, inline=False)
    embed.add_field(name='Roles:', value=list)

    await ctx.send(embed=embed)





@commands.command()
async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]**\n"

        if (a == b == c):
            await ctx.send(f"{slotmachine} ``WINNER WINNER CHICKEN DINNER!`` 🎉")
        else:
            await ctx.send(f"{slotmachine} aww you lost! 😢")








@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responces = ['Yes',
                 'Yessir',
                 'Squirt first 😳',
                 'Naw',
                 'Maybe',
                 'Green',
                 'Not at all bro']
    await ctx.send(f'``Question: {question}\nAnswer``: {random.choice(responces)}')





 @client.command()
    async def fact(self):
        url = f'https://uselessfacts.jsph.pl/random.json?language=en'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r['text']
                embed = discord.Embed(title=f'***Random Fact***', colour=ctx.author.colour, timestamp=ctx.message.created_at)

                embed.add_field(name='**Fun Fact**', value=fact, inline=False)
                await ctx.send(embed=embed)





      

client.run(os.environ['DISCORD_TOKEN'])