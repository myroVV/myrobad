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
                await ctx.send(embed=embed)




    @commands.command()
    async def insta(self, ctx, username):
        url = f'https://apis.duncte123.me/insta/{username}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                data = r['user']
                username = data["username"]
                followers = data["followers"]["count"]
                following = data["following"]["count"]
                uploads = data["uploads"]["count"]
                biography = data["biography"]
                private = data["is_private"]
                verified = data["is_verified"]

                embed = discord.Embed(title=f'Insta Details: {username}')
                embed.add_field(name='Bio', value=biography + '\u200b', inline=False)
                embed.add_field(name='Private Status', value=private, inline=False)
                embed.add_field(name='Verified Status', value=verified, inline=False)
                embed.add_field(name='Followers', value=followers, inline=False)
                embed.add_field(name='Following', value=following, inline=False)
                embed.add_field(name='Posts', value=uploads, inline=False)
                await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Misc(client))
