import discord
import os
import random
from time import sleep
import time
from discord import Spotify
from pathlib import Path
import asyncio
from aiohttp import ClientSession
import aiohttp
from discord.ext import commands, tasks
from random import choice
from discord.voice_client import VoiceClient
from datetime import datetime
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown


client = discord.Client()

client = commands.Bot(command_prefix=".")
client.remove_command("help")



@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Whole Lotta Red"))
    print('Bot is online')


@client.command()
async def coinflip(ctx):
    choices = ["``Heads``", "``Tails``"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


@client.command(aliases=['cl'])
async def clear(ctx, amount=7):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = f"{member.name}'s avatar", color = member.color , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by : {ctx.author}",icon_url=ctx.author.avatar_url)  
    await ctx.send(embed=embed)







@client.command()
async def members(ctx):
    await ctx.send("``Membercount : {0.member_count}``".format(ctx.message.guild))





@client.command(pass_context=True)
async def hack(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("``Please specify a user!``")
        return

    passwords=['dousquirt','sendnoodes63','ilovenood-','myrotrashcoder','unblacklistmyro','hackedlol','quickied','insta2dpce','kookikooki','69'] 
    fakeips=['154.2345.24.743','255.255. 255.0','356.653.56','101.12.8.6053','255.255. 255.0']

    embed=discord.Embed(title=f"**Hacking: {member}** 0%", color=0x2f3136)
    m = await ctx.send(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 19%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 34%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 55%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 67%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 84%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 99%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 100%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(3)
    embed=discord.Embed(title=f"{member}'s info ", description=f"**Email: `{member}@hacked.com` Password: `{random.choice(passwords)}`  IP: `{random.choice(fakeips)}`**", color=0x2f3136)
    embed.set_footer(text="Sending Insta 2s to your house! 😈")
    await m.edit(embed=embed)
    time.sleep(1)






@client.command(aliases=['8ball'])
@commands.cooldown(1, 3, commands.BucketType.guild)
async def _8ball(ctx, *, question):
    responces = ['Yes',
                 'Yessir',
                 'Squirt first 😳',
                 'Naw',
                 'Maybe',
                 'Idk bro you ask me',
                 'Ur mom lol',
                 'Stfu dumb retard',
                 'Dude no lol',
                 'No way Jose',
                 'DA VINKI?',
                 'Not at all bro']
    await ctx.send(f'``Question:`` **{question}**\n``Answer``: **{random.choice(responces)}**')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '``This command is on cooldown, please try again in {:.2f}s``'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error




@client.command()
async def boop (ctx, member:discord.User=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("``You cannot boop yourself``")
        return
    await ctx.channel.send(f"``✅ {member} Has been successfully booped! ✅``")

  




@client.command(description="Bot's latency.")
async def ping(ctx):
    latency = round(client.latency * 1000, 1)
    await ctx.send(f"``Pong! {latency}ms``")




@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="More commands coming soon!", color=0x6da860, timestamp=datetime.utcnow())
    embed.add_field(name="**Mod**", value=f"``.kick`` ``.ban`` ``.mute`` ``.lock``", inline=False)
    embed.add_field(name="**Fun**", value=f"``.8ball`` ``.iq`` ``.ego`` ``.pp`` ``.potacc`` ``.potaccuracy`` ``.hack`` ``.slot`` ``.fact`` ``.gay`` ", inline=False)
    embed.add_field(name="**Info**", value=f"``.av`` ``.avatar`` ``.userinfo`` ``.covid`` ``.news``", inline=False)
    embed.set_footer(text=f"Suggested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)







###############################music#####################################


import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


client = commands.Bot(command_prefix='?')

status = ['Jamming out to music!', 'Eating!', 'Sleeping!']
queue = []



@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `RK Coding`')
    await ctx.send('Thanks to `DiamondSlasher` for coming up with the idea')
    await ctx.send('Thanks to `KingSticky` for helping with the `?die` and `?creditz` command')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')

@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='play', help='This command plays songs')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))





client.run(os.environ['DISCORD_TOKEN'])