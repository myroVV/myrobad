import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="My Stream", url=https://www.youtube.com/channel/UCibHDZGIxI7taVblvdeOB4w?view_as=subscriberl))
    print('Bot is online')


client.run(os.environ['DISCORD_TOKEN'])