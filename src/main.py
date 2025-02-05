import os
import signal
import sys
import asyncio
import time

import discord
from discord.ext import commands
from discord import app_commands

from myBotInfo import botToken
from myBotInfo import myServerID

import View.messagesForTerminal as messagesForTerminal

messagesForTerminal.cleanTerminal()
messagesForTerminal.botLoadingMessage()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=myServerID))
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.botIsReadyForUseMessage()
    
async def closeBot():
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.closingBotMessage()
    await bot.close()
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.botIsClosedMessage()
    messagesForTerminal.cleanTerminal()

def redirectSignalToCloseBot(signum, frame):
    asyncio.create_task(closeBot())

signal.signal(signal.SIGINT, redirectSignalToCloseBot)
try:
    bot.run(botToken)
finally:
    sys.exit(0)