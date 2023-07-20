import asyncio
import discord
from discord.ext import commands
from discordbot.botapp.config import TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

cogslist = ["verification"]


def load_cogs():
    for cog in cogslist:
        asyncio.run(load_cog(cog))


async def load_cog(cog_name):
    await bot.load_extension(f"discordbot.botapp.cogs.{cog_name}")


load_cogs()
bot.run(TOKEN)
