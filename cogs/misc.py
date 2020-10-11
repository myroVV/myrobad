import discord
from discord.ext import commands
import asyncio
import requests
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



    @commands.command(aliases=['Meme', "M"])
    async def meme(self, msg:commands.Context):
        fetch:discord.Message = await msg.channel.send("Getting a meme...")
        req = requests.request("GET",'https://apis.duncte123.me/meme')
        meme = req.json()
        emb = discord.Embed()
        emb.set_image(url=meme["data"]["image"])
        emb.add_field(name="Quality meme", value=f'[{meme["data"]["title"]}]({meme["data"]["url"]})')
        await fetch.edit(embed=emb)



def setup(client):
    client.add_cog(Misc(client))
