import discord
from discord.ext import commands
from discord import app_commands

from myBotInfo import myServerID

from Model.robuxCalculator import calculateRobux
from Data.robuxImage import robuxImage

class Robux(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="robux_price", description="Calcula o preço de um determinado valor de robux em reais")
    async def calculateRobuxPrice(self, interaction: discord.Interaction, amount: int):
        robuxPrice = calculateRobux(amount)
        robuxGroupPrice = robuxPrice[0]
        robuxGamepassPrice = robuxPrice[1]
        
        embed = discord.Embed(
            title=f"Preço de {amount} Robux em Reais",
            description=f"Abaixo estão os preços calculados para {amount} Robux:",
            color=discord.Color.blue()  # A cor do embed
        )
        embed.add_field(
            name="Preço por grupo:", 
            value=f"R$ {robuxGroupPrice:.2f}", 
            inline=True
        )
        embed.add_field(
            name="Preço por Gamepass:", 
            value=f"R$ {robuxGamepassPrice:.2f}", 
            inline=True
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        embed.set_thumbnail(url=robuxImage)
        
        await interaction.response.send_message(embed=embed)

    async def cog_load(self):
        guild = discord.Object(id=myServerID)
        self.bot.tree.add_command(self.calculateRobuxPrice, guild=guild)

async def setup(bot): 
    await bot.add_cog(Robux(bot))
