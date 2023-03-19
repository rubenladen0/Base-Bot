import discord, os
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension(f"cogs.moderation")
    await bot.load_extension(f"cogs.general")
    print(f"Bot en ligne !")
    await bot.tree.sync()


bot.run(token) 








    
    


