# Libs
import discord
from discord.ext import commands
import json
from pathlib import Path
import logging
import datetime
import os

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#Defining a few things
bot = commands.Bot(command_prefix='%', case_insensitive=True, owner_id=213978971191115776)
bot.config_token = ['DISCORD_TOKEN']
logging.basicConfig(level=logging.INFO)

bot.blacklisted_users = []
bot.cwd = cwd

bot.version = '5'

bot.colors = {
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_NAVY': 0x2C3E50
}
bot.color_list = [c for c in bot.colors.values()]

# amazing
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('myro > all'))
    print ('Online')

@bot.event
async def on_message(message):
    #Ignore messages sent by yourself
    if message.author.id == bot.user.id:
        return

    #A way to blacklist users from the bot by not processing commands if the author is in the blacklisted_users list
    if message.author.id in bot.blacklisted_users:
        return

    await bot.process_commands(message)

if __name__ == '__main__':
    # When running this file, if it is the 'main' file
    # I.E its not being imported from another python file run this
    for file in os.listdir(cwd+"/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

client.run(os.environ['DISCORD_TOKEN'])