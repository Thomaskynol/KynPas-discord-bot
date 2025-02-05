from datetime import datetime

import discord
from discord.ext import commands
from discord import app_commands

from myBotInfo import myServerID

import View.messagesForTerminal as messagesForTerminal
from Model.rolesPermissions import manageTickets as manageTicketsRole

class TicketPanel(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__(timeout=None)
        
        support_roles = [
            discord.utils.get(interaction.guild.roles, id=1320534883088466036),
            discord.utils.get(interaction.guild.roles, id=1320534883088466035),
            discord.utils.get(interaction.guild.roles, id=1320534883088466034)
        ]
        mentions = " ".join(role.mention for role in support_roles if role)
        
        creator = interaction.user
        
        self.embed = discord.Embed(
            title=f"Ticket #{creator.name}",
            color=0x2b2d31
        )
        self.embed.add_field(
            name="Criado por",
            value=f"{creator.mention}\n`({creator.id})`",
            inline=True
        )
        self.embed.add_field(
            name="Data de criação",
            value=discord.utils.format_dt(datetime.now(), "F"),
            inline=True
        )
        self.embed.add_field(
            name="Status",
            value="🔓 **Aberto**",
            inline=False
        )
        self.embed.add_field(
            name="Atendimento",
            value=f"Um de nossos {mentions} irá atendê-lo em breve.",
            inline=False
        )
        self.embed.add_field(
            name="Instruções",
            value="• Envie a quantidade de Robux que deseja\n• Informe o método de transferência(gamepass ou grupo)\n• Envie seu nome de usuário do Roblox\n• Realize o pagamento\n• Receba os robux!",
            inline=False
        )
        
    @discord.ui.button(label="Fechar Ticket", style=discord.ButtonStyle.red, emoji="❌", custom_id="close_ticket")
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        messagesForTerminal.botLogMessage(f"Ticket {interaction.channel.name} fechado por {interaction.user.name} ({interaction.user.id})")
        await interaction.response.send_message("Ticket fechado.", ephemeral=True)
        await interaction.channel.delete()


class TicketCreationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.embed = discord.Embed(
            title="Comprar Robux - Ticket",
            description="Clique no botão abaixo para iniciar seu pedido",
            color=0x2b2d31  # dark gray
        )
        
        self.embed.add_field(
            name="Passo a Passo",
            value="1. Abra um ticket\n2. Mande as informações pedidas\n3. Fassa o pagamento\n4. Receba os Robux",
            inline=False
        )
    
        self.embed.add_field(
            name="Aviso",
            value="• Pagamentos somente via PIX",
            inline=False
        )

    @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.green, emoji="🎫", custom_id="abrir_ticket")
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        category = discord.utils.get(interaction.guild.categories, name="tickets")
        if not category:
            category = await interaction.guild.create_category("tickets")

        existing_ticket = discord.utils.get(category.text_channels, name=f"ticket-{interaction.user.id}")
        if existing_ticket:
            await interaction.response.send_message(
                f"Você já possui um ticket aberto: {existing_ticket.mention}.", ephemeral=True
            )
            return

        ticket_channel = await interaction.guild.create_text_channel(f"ticket-{interaction.user.id}",category=category)
        
        await ticket_channel.set_permissions(interaction.guild.default_role, view_channel=False)
        await ticket_channel.set_permissions(interaction.user, view_channel=True)
        messagesForTerminal.botLogMessage(f"Ticket criado por {interaction.user.name} ({interaction.user.id})")
        
        view = TicketPanel(interaction)
        await ticket_channel.send(
            embed=view.embed, view=view 
        )
        await interaction.response.send_message(f"Seu ticket foi criado: {ticket_channel.mention}", ephemeral=True)

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_creation_tickets_embed", description="Cria um embed para criação de tickets")
    async def createCreationTicketsEmbed(self, interaction: discord.Interaction):
        if not discord.utils.get(interaction.user.roles, name=manageTicketsRole):
            await interaction.response.send_message("Você não tem permissão para executar este comando.", ephemeral=True)
            return
        view = TicketCreationView()
        await interaction.response.send_message(embed=view.embed, view=view)

    async def cog_load(self):
        guild = discord.Object(id=myServerID)
        self.bot.tree.add_command(self.createCreationTicketsEmbed, guild=guild)

async def setup(bot): 
    await bot.add_cog(Tickets(bot))
