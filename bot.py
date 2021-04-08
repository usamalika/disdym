import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('bot ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('.Hello juga!')

client.run('ODI4NzgyOTQ5NjcxNTAxODg2.YGumRQ.bRXpOY1RQxmPV1wRBazjYOZ7ENs')