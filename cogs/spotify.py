import discord
import pendulum
import spotify
from discord.ext import commands


class Spotify(commands.Cog):
    """
    spoopifyXD
    """

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Spotify Cog has been loaded\n-----")



    @commands.command()
    async def spotify(self, ctx, user: discord.Member=None):
        user = user or ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                em = discord.Embed(color=activity.color)
                em.title = f'{user.name} is listening to {activity.title}'
                em.set_thumbnail(url=activity.album_cover_url)
                em.description = f"**Song Name**: {activity.title}\n**Song Aetist**: {activity.artist}\n**Song Album**: {activity.album}\n**Song Lenght**: {pendulum.duration(seconds=activity.duration.total_seconds()).in_words(locale='en')}"
                await ctx.send(embed=em)
                break
        else:
            embed = discord.Embed(color=0xff0000)
            embed.title = f'{user.name} is not listening Spotify right now!'
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Spotify(client))
