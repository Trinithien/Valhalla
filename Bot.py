# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.member.status)
   # print(client.user(166164767701073921).status)

@client.event
async def on_message(message):
    print(message.author.id)
    print(message.author.status)




client.run(TOKEN)




