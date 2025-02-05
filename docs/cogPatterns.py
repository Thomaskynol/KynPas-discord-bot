import discord
from discord.ext import commands
from discord import app_commands

serverID = 123456789

class cogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        guild = discord.Object(id=serverID)
        self.bot.tree.add_command(self.calculateRobuxPrice, guild=guild)

async def setup(bot): 
    await bot.add_cog(cogName(bot))
