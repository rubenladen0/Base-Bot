import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="ping", description="Savoir mon ping")
    async def ping(self, i: discord.Interaction):
        png = self.bot.latency
        while len(str(png))>5:
            png = str(png)[:-1]
            
        await i.response.send_message(f"Mon ping est d'environ {str(png)} ms !")
        
    @app_commands.command(name="help", description="Voir mes commandes")
    async def help(self, i: discord.Interaction):
        embed = discord.Embed(title="Help", timestamp=datetime.now(), description="Voici mes commandes avec comme préfix `/`: \n\n**Générale :**\n`ping` - Avoir mon ping\n`help` - Avoir ce menu\n`info` - Information sur le bot\n\n**Modération :**\n`clear` - Supprimer des messages\n`kick` - Kick un membre\n`ban` - Bannir un membre\n`unban` - Débannir un membre")
        await i.response.send_message(embed=embed)
    
    @app_commands.command(name="info", description="Informations sur le bot")
    async def info(self, i: discord.Interaction):
        mess = "Langage: Python\nLibrairie: Discord.py\nBot Open Source: [Github](https://github.com/NX-GoldJust/Base-Bot)"
        embed = discord.Embed(title="Info", description=mess, timestamp=datetime.now())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await i.response.send_message(embed=embed)
        
        
        
        
        
        
        
        
        
async def setup(bot):
    await bot.add_cog(General(bot))
