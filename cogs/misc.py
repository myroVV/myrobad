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



    @commands.command(aliases=['lock'])
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel=None):
            channel = channel or ctx.channel

            if ctx.guild.default_role not in channel.overwrites:
                overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
                }
                await channel.edit(overwrites=overwrites)
                embed = discord.Embed(title="Channel locked", description="⛓️", color=0x6da860)
                await ctx.send(embed=embed)
            elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
                overwrites = channel.overwrites[ctx.guild.default_role]
                overwrites.send_messages = False
                embed = discord.Embed(title="Channel locked", description="⛓️", color=0x6da860)
                await ctx.send(embed=embed)
            else:
                overwrites = channel.overwrites[ctx.guild.default_role]
                overwrites.send_messages = True
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
                embed = discord.Embed(title="Channel unlocked", description="⛓️", color=0x6da860)
                await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Misc(client))
