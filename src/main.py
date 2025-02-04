import View.messagesForTerminal as messagesForTerminal
messagesForTerminal.cleanTerminal()
messagesForTerminal.botLoadingMessage()

import os

import discord
from discord.ext import commands
from discord import app_commands

from myBotInfo import botToken
from myBotInfo import serverID

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=serverID))
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.botIsReadyForUseMessage()
    
def closeBot():
    messagesForTerminal.closingBotMessage()
    bot.close()
    messagesForTerminal.botIsClosedMessage()
    os._exit(0)
    
