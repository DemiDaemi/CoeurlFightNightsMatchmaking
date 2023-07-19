import discord
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    author = message.author
    channel = message.channel


# IMPORTANT: You shouldn't hard code your token
# these are very important, and leaking them can
# let people do very malicious things with your
# bot. Try to use a file or something to keep
# them private, and don't commit it to GitHub
client.run(config.TOKEN)
