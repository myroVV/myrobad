import discord
import os
import random
from time import sleep
import time
import pendulum
from discord import Spotify
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
    embed=discord.Embed(title=f"{member} info ", description=f"*Email `{member}@hacked.com` Password `{random.choice(passwords)}`  IP `{random.choice(fakeips)}`*", color=0x2f3136)
    embed.set_footer(text="Sending Insta 2's to your house 😈.")
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
                '8================D **16 inches 📏**'
                '8=================D **17 inches 📏**'
                '8==================D **18 inches 📏**'
                '8===================D **19 inches 📏**'
                '8==============================D **30 inches 😵**'
                '8===============================D **31 inches 😵😵**'
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

    embed = discord.Embed(title=f'{ctx.author.name}', description=f"This shows the User Info of {ctx.author.name}", colour=ctx.author.colour)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name='Discord Tag:', value=ctx.author, inline=True)
    embed.add_field(name='Nick:', value=ctx.author.nick, inline=True)
    embed.add_field(name='Status:', value=ctx.author.status,inline=True )
    embed.add_field(name='ID:', value=ctx.author.id, inline=False)
    embed.add_field(name='Created On:', value=ctx.author.created_at, inline=False)
    embed.add_field(name='Joined:', value=ctx.author.joined_at, inline=False)
    embed.add_field(name='Roles:', value=list)

    await ctx.send(embed=embed)













@client.command()
async def np(self, ctx, user: discord.Member=None):
      if user is None:
          user=ctx.author
      for activity in user.activities:
          if isinstance(activity, Spotify):
              embed=discord.Embed(title=activity.title, description=activity.artist, color=activity.color)
              embed.set_thumbnail(url=activity.album_cover_url)
              embed.add_field(name=activity.album, value=(f"Song Length: {pendulum.duration(seconds=activity.duration.total_seconds()).in_words(locale='en')}"), inline=True)
              embed.set_footer(text="myrosaurus | Spotify")
              await ctx.send (embed=embed)
              break
      else:
          await ctx.send(f"{user.mention} ``Is not listening to music atm``")






client.run(os.environ['DISCORD_TOKEN'])