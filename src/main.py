import os
import signal
import sys
import asyncio
import time

import discord
from discord.ext import commands

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
    await loadCogs()
    await bot.tree.sync(guild=discord.Object(id=myServerID))
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.botIsReadyForUseMessage()
    
def startBot():
    signal.signal(signal.SIGINT, redirectSignalToCloseBot)
    try:
        bot.run(botToken)
    finally:
        sys.exit(0)
    
async def closeBot():
    messagesForTerminal.cleanTerminal()

    messagesForTerminal.closingBotMessage()
    await bot.close()
    messagesForTerminal.cleanTerminal()
    messagesForTerminal.botIsClosedMessage()
    messagesForTerminal.cleanTerminal()

def redirectSignalToCloseBot(signum, frame):
    asyncio.create_task(closeBot())

async def loadCogs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    controllers_path = os.path.join(script_dir, 'Controllers')

    for filename in os.listdir(controllers_path):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'Controllers.{filename[:-3]}')
            messagesForTerminal.loadedCogMessage(filename[:-3])
            
async def loadPersistence():
    pass

startBot()