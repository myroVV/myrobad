import discord
from discord.ext import commands
import asyncio
from aiohttp import ClientSession

class Misc(commands.Cog):
    """
    funsz
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Misc Cog has been loaded\n-----")



    @commands.command()
    async def fact(self, ctx):
        url = f'https://uselessfacts.jsph.pl/random.json?language=en'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r['text']
                embed = discord.Embed(title=f'***Random Fact***', colour=ctx.author.colour, timestamp=ctx.message.created_at)

                embed.add_field(name='**Fun Fact**', value=fact, inline=False)


    @commands.command(aliases=['userinfo, info'])
    async def whois (self, ctx):

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



def setup(client):
    client.add_cog(Misc(client))
