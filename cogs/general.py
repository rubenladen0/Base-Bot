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
        embed = discord.Embed(title="Help", timestamp=datetime.now(), description="Voici mes commandes avec comme préfix `/`: \n\n**Générale :**\n`ping` - Avoir mon ping\n`help` - Avoir ce menu\n`info` - Information sur le bot\n`say` - Envoyer un message avec le bot(admin)\n\n**Modération :**\n`clear` - Supprimer des messages\n`kick` - Kick un membre\n`ban` - Bannir un membre\n`unban` - Débannir un membre\n`off` - Mettre off le bot")
        await i.response.send_message(embed=embed)
    
    @app_commands.command(name="info", description="Informations sur le bot")
    async def info(self, i: discord.Interaction):
        mess = "Langage: Python\nLibrairie: Discord.py\nBot Open Source: [Github](https://github.com/NX-GoldJust/Base-Bot)"
        embed = discord.Embed(title="Info", description=mess, timestamp=datetime.now())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await i.response.send_message(embed=embed)
        
    @app_commands.command(name="say", description="Envoyer un message avec l'identité du bot")
    @app_commands.describe(message="Le message")
    @app_commands.describe(salon="Le salon")
    @app_commands.default_permissions(administrator=True)
    async def say(self, i: discord.Interaction, message: str, salon: discord.TextChannel=None):
        if not salon:
            salon = i.channel
        embed = discord.Embed(title=None, description=message, timestamp=datetime.now())
        embed.set_footer(text=i.user.name, icon_url=i.user.avatar.url)
        await salon.send(embed=embed)
        await i.response.send_message("Message envoyé", ephemeral=True)
        
        
async def setup(bot):
    await bot.add_cog(General(bot))
