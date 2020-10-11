import discord
from discord.ext import commands

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
    async def serverinfo(self, ctx):
            """Shows server info"""

            server = ctx.message.server

            roles = str(len(server.roles))
            emojis = str(len(server.emojis))
            channels = str(len(server.channels))

            embeded = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
            embeded.set_thumbnail(url=server.icon_url)
            embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
            embeded.add_field(name="Server ID:", value=server.id, inline=False)
            embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
            embeded.add_field(name="Server owner:", value=server.owner, inline=True)

            embeded.add_field(name="Default Channel:", value=server.default_channel, inline=True)
            embeded.add_field(name="Server Region:", value=server.region, inline=True)
            embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)

            embeded.add_field(name="Role Count:", value=roles, inline=True)
            embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
            embeded.add_field(name="Channel Count:", value=channels, inline=True)

            await self.client.say(embed=embeded)


def setup(client):
    client.add_cog(Misc(client))
