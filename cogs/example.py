import discord
from discord.ext import commands
import asyncio
from aiohttp import ClientSession

class Example(commands.Cog):
#need
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

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


#NEED
def setup(client):
    client.add_cog(Example(client))