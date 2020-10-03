# Standard libraries
import discord
from discord.ext import commands
import os
import pyautogui, time

f = open("despise, 'r'")
    pyautogui.typewrite(word)
    pyautogui.press("enter")

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('I despise luna'))
    print('Bot is online')

@client.event
async def on_message(message):

     if "no one asked" in message.content:
           await Bot.send_message(message.channel, 'I asked wdym u mean')

           


client.run(os.environ['DISCORD_TOKEN'])
