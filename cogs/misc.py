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






    @commands.command(pass_context=True, aliases=['uinfo'])
    async def userinfo(self, ctx, user: discord.Member=None):
        user = user or ctx.message.author
        embed = discord.Embed(title=f"{user}'s info", color=0xffffff)
        embed.add_field(name="User info:", value=f'Username: **{user.name + "#" + user.discriminator}**\nID: **{user.id}**\nRegistered: **{user.created_at.strftime("%a, %d %b %Y %I:%M %p")}**\nStats: {user.status}\nBot: **{user.bot}**', inline=False)
        embed.add_field(name="Member info", value=f'Nickname: **{user.nick}**\nJoined date: **{user.joined_at.strftime("%a, %d %b %Y %I:%M %p")}**\nHighest Role: **{user.top_role}**', inline=False)                
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))
