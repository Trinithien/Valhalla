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
    #Henter alle medlemene den har tilgang til.
    members = client.get_all_members()
    #For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        #Hvis statusen per medlem er det samme som status online printer vi den personen.
        if member.status == discord.Status.online:
            print(member)


# print(client.user(166164767701073921).status)

@client.event
async def on_message(message):
    print(message.author.id)
    print(message.author.status)


client.run(TOKEN)
