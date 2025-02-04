import discord
from discord.ext import commands
from discord import app_commands
from myBotInfo import botToken
from myBotInfo import serverID
import View.MessagesForTerminal as MessagesForTerminal

MessagesForTerminal.cleanTerminal()
MessagesForTerminal.botLoadingMessage()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    MessagesForTerminal.cleanTerminal()
    MessagesForTerminal.botIsReadyForUseMessage()
    await bot.change_presence(activity=discord.Game(name="!help"))