from io import BytesIO

import discord
from discord.ext import commands
from discord import app_commands

from myBotInfo import myServerID

from Model.generatePix import generatePix

class Payments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate_pix_qrcode", description="Gera um qrcode pix com um valor pré-definido")
    async def generatePixQRCODE(self, interaction: discord.Interaction, price: float, robux_amount: int):
        pixCopyPaste, pixQrCode = generatePix(price, robux_amount)
        
        with BytesIO() as buffer:
            pixQrCode.save(buffer, format="PNG")
            buffer.seek(0)
            discord.File(buffer, filename="pixQrCode.png")
            
            embed = discord.Embed(
                title=f"Pagamento com Pix - {robux_amount} Robux",
                description=f"Abaixo estão os detalhes do pagamento para {robux_amount} Robux. "
                            f"Para concluir a compra, utilize o QR Code Pix abaixo ou copie o código.",
                color=discord.Color.green()
            )
            embed.add_field(
                name="Valor a ser pago:", 
                value=f"R$ {price:.2f}", 
                inline=True
            )
            embed.add_field(
                name="Forma de pagamento:", 
                value="Pix", 
                inline=True
            )
            embed.add_field(
                name="Código Pix:", 
                value=f"```{pixCopyPaste}```", 
                inline=False
            )
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
            embed.set_image(url="attachment://pixQrCode.png")
            
            await interaction.response.send_message(embed=embed, file=discord.File(buffer, filename="pixQrCode.png"))
        
    async def cog_load(self):
        guild = discord.Object(id=myServerID)
        self.bot.tree.add_command(self.generatePixQRCODE, guild=guild)

async def setup(bot):
    await bot.add_cog(Payments(bot))