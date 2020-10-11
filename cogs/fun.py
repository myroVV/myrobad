from discord.ext import commands
from aiohttp import ClientSession
import discord
import random

class Fun(commands.Cog):
    """
    funsz
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog has been loaded\n-----")


    @commands.command()
    async def slot(self, ctx):
            emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
            a = random.choice(emojis)
            b = random.choice(emojis)
            c = random.choice(emojis)

            slotmachine = f"**[ {a} {b} {c} ]**\n"

            if (a == b == c):
                await ctx.send(f"{slotmachine} ``WINNER WINNER CHICKEN DINNER 🎉🎉🎉`` ")
            else:
                await ctx.send(f"{slotmachine} u lost lol 😢")


    @commands.command(help='Shows top News Story')
    async def news(self, ctx):
        key = 'd84cca93f77a4df7a3eb3c91f5775aa1'
        url = f'https://newsapi.org/v2/top-headlines?country=au&apiKey={key}'
        print(url)
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                firstArticle = r['articles'][0]
                nSource = firstArticle['source']['name']
                nTitle = firstArticle['title']
                nTimestamp = firstArticle['publishedAt']
                embed = discord.Embed(title=f'News Title: {nTitle}', description=f'News Source: {nSource}')
                embed.add_field(name='News Content', value=firstArticle['description'])
                #embed.set_image(url=firstArticle['urlToImage'])
                embed.set_footer(text=f'News Timestamp: {nTimestamp}')
                await ctx.send(embed=embed)



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



def setup(client):
    client.add_cog(Fun(client))
