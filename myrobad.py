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
    await ctx.channel.send(f"``✅ {member} **Has been successfully booped! ✅**")


      







class Covid(commands.Cog):
    """
    Covid API Commands!
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Covid Cog has been loaded\n-----")

    @commands.group(help= 'Base command')
    async def covid(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please use a valid Option `ALl`, `Country`, `Continent`")


    @covid.group(help= 'Gets information of Covid-19 stats of a country')
    async def country(self, ctx, country1):
        url = f'https://disease.sh/v3/covid-19/countries/{country1}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                html = await response.json()
                data = [html]

                #getting data from API then format to readable numbers
                test = data[0]["countryInfo"]["flag"]
                population = data[0]["population"]
                population_format = format(population, ",")
                country = data[0]["country"]
                cases = data[0]["cases"]
                cases_format = format(cases, ",")
                deaths = data[0]["deaths"]
                deaths_format = format(deaths, ",")
                active = data[0]["active"]
                active_format = format(active, ",")
                recovered = data[0]["recovered"]
                recovered_format = format(recovered, ",")
                critical = data[0]["critical"]
                critical_format = format(critical, ",")
                tests = data[0]["tests"]
                tests_format = format(tests, ",")


                #making stats
                fatality = deaths/cases*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = cases/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/cases*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'Covid Details: {country}')
                embed.set_thumbnail(url=test)
                embed.add_field(name='Total Cases', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Total Deaths', value=deaths_format, inline=True)
                embed.add_field(name='Active', value=active_format, inline=True)
                embed.add_field(name='Recovered', value=recovered_format, inline=True)
                embed.add_field(name='Critical', value=critical_format, inline=True)
                embed.add_field(name='Tests', value=tests_format, inline=True)
                embed.add_field(name='Population', value=population_format, inline=True)
                embed.add_field(name='Infection Rate', value=infected_rate_percent, inline=True)
                embed.add_field(name='Fatality Rate', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Critical Rate', value=critical_rate_percent, inline=True)
                embed.add_field(name='Recovery Rate', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Rate', value=test_rate_percent, inline=True)
                await ctx.send(embed=embed)

    @covid.group(help= 'Gets Summary of All countries with Covid-19')
    async def all(self, ctx):
        url = f'https://disease.sh/v3/covid-19/all'
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                #getting data from API then format to readable numbers
                case = data['cases']
                cases_format = format(case, ",")

                population = data["population"]
                population_format = format(population, ",")

                deaths = data["deaths"]
                deaths_format = format(deaths, ",")

                active = data["active"]
                active_format = format(active, ",")

                recovered = data["recovered"]
                recovered_format = format(recovered, ",")

                critical = data["critical"]
                critical_format = format(critical, ",")

                tests = data["tests"]
                tests_format = format(tests, ",")

                infected_countries = data['affectedCountries']


               


                #making stats
                fatality = deaths/case*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = case/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/case*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'Covid Details All')
                embed.set_thumbnail(url='https://i2x.ai/wp-content/uploads/2018/01/flag-global.jpg')
                embed.add_field(name='Total Cases', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Total Deaths', value=deaths_format, inline=True)
                embed.add_field(name='Active', value=active_format, inline=True)
                embed.add_field(name='Recovered', value=recovered_format, inline=True)
                embed.add_field(name='Critical', value=critical_format, inline=True)
                embed.add_field(name='Tests', value=tests_format, inline=True)
                embed.add_field(name='Population', value=population_format, inline=True)
                embed.add_field(name='Infection Rate', value=infected_rate_percent, inline=True)
                embed.add_field(name='Fatality Rate', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Critical Rate', value=critical_rate_percent, inline=True)
                embed.add_field(name='Recovery Rate', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Rate', value=test_rate_percent, inline=True)
                embed.add_field(name='Infected Countries', value=infected_countries, inline=True)
                await ctx.send(embed=embed)

    @covid.group(help= 'Gets Summary of a continent with Covid-19')
    async def continent(self, ctx, continent):
        url = f'https://disease.sh/v3/covid-19/continents/{continent}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                #getting data from API then format to readable numbers
                case = data['cases']
                cases_format = format(case, ",")

                population = data["population"]
                population_format = format(population, ",")

                deaths = data["deaths"]
                deaths_format = format(deaths, ",")

                active = data["active"]
                active_format = format(active, ",")

                recovered = data["recovered"]
                recovered_format = format(recovered, ",")

                critical = data["critical"]
                critical_format = format(critical, ",")

                tests = data["tests"]
                tests_format = format(tests, ",")

                countries = data['countries']


                #making stats
                fatality = deaths/case*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = case/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/case*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'Covid Details of {continent}')
                embed.set_thumbnail(url='https://i2x.ai/wp-content/uploads/2018/01/flag-global.jpg')
                embed.add_field(name='Total Cases', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Total Deaths', value=deaths_format, inline=True)
                embed.add_field(name='Active', value=active_format, inline=True)
                embed.add_field(name='Recovered', value=recovered_format, inline=True)
                embed.add_field(name='Critical', value=critical_format, inline=True)
                embed.add_field(name='Tests', value=tests_format, inline=True)
                embed.add_field(name='Population', value=population_format, inline=True)
                embed.add_field(name='Infection Rate', value=infected_rate_percent, inline=True)
                embed.add_field(name='Fatality Rate', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Critical Rate', value=critical_rate_percent, inline=True)
                embed.add_field(name='Recovery Rate', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Rate', value=test_rate_percent, inline=True)
                embed.add_field(name='Countries', value=countries, inline=True)

                await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Covid(client))




client.run(os.environ['DISCORD_TOKEN'])