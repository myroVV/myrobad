import discord
from discord.ext import commands


class userinfo(commands.Cog):
    """
    Covid API Commands!
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("userinfo Cog has been loaded\n-----")

@commands.command()
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





def setup(client):
    client.add_cog(Covid(client))