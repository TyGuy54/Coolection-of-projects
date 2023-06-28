import os
import discord
import random
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.command(name='joke')
async def funny_joke(ctx):
    
    random_joke = random.randint(0, 100)
    get_joke = requests.get(f"https://official-joke-api.appspot.com/jokes/{random_joke}")

    response = get_joke.json()

    await ctx.send(response["setup"])
    await ctx.send(response["punchline"])

bot.run(TOKEN)