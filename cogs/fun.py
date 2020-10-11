from discord.ext import commands
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


def setup(client):
    client.add_cog(Fun(client))
