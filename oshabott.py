import discord
import os
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from constants import ENV_PATH
from constants import COGS_PATH

# grab discord bot token from .env file
load_dotenv(ENV_PATH, encoding='utf-8')
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN is not found')

@bot.event
async def on_ready():
    print("Oshabott is online!")

async def load_cogs():
    for filename in os.listdir(COGS_PATH):
        if filename.endswith('.py') and not filename.startswith('__'): # ensure that file is not __init__ and python file
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_cogs()
    await bot.start(BOT_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())