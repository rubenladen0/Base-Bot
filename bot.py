import discord, os
from discord.ext import commands
from config import *

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension(f"cogs.moderation")
    print(f"Bot en ligne !")
    await bot.tree.sync()


bot.run(token) 








    
    


