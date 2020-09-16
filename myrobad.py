import discord
from discord.ext import commands
import asyncio
import os

client = discord.Client()

bot = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print ('Online')

@client.event
async def on_message(message):
    if message.author.id == 701974976911245382:
        return

async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
    roleobject = discord.utils.get(ctx.message.guild.roles, id=730016083871793163)
    await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
    await user.add_roles(roleobject)
    if unit == "s":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m":
        wait = 60 * duration
        await asyncio.sleep(wait)
    await user.remove_roles(roleobject)
    await ctx.send(f":white_check_mark: {user} was unmuted")    

client.run(os.environ['DISCORD_TOKEN'])