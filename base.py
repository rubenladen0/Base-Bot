#Import nécessaire
import discord
from discord.ext import commands

#Définition du bot:
client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None) #remplacer le ! par votre prefix


@client.event  #event 
async def on_ready():  #Au moment où le bot est en ligne
    print("Bot en ligne !") #Il écrit que c'est bon
    await bot.tree.sync() #activation des slash command

client.run("TOKEN")#Mettez le token bien entre "
