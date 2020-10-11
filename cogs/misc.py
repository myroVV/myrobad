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



    @commands.command(aliases=['userinfo'])
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed=discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Member Name:", value=member.display_name)
        embed.add_field(name="Created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top Role:", value=member.top_role.mention)
        embed.add_field(name="Bot", value=member.bot)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Misc(client))
