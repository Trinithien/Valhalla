# bot.py
import os
import sched, time
from threading import Timer

import discord
from discord.ext import tasks, commands

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
s = sched.scheduler(time.time, time.sleep)


def check_online():
    # Henter alle medlemene den har tilgang til.
    members = 0
    members = client.get_all_members()
    # For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        # Hvis statusen per medlem er det samme som status online printer vi den personen.
        if member.status == discord.Status.online:
            print(member)
        else:
            print(member, 'offline')
    Timer(5.0,check_online).start() # Method calls itself again after 60 seconds

    


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    check_online()
    #s.enter(5, 1, check_online, (s,))
    #s.run()

@client.event
async def on_message(message):
    print(message.author.id)
    print(message.author.status)
    members = client.get_all_members()
    # For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        # Hvis statusen per medlem er det samme som status online printer vi den personen.
        if member.status == discord.Status.online:
            print(member)

from discord.ext import commands, tasks
bot = commands.Bot(command_prefix='-')

@tasks.loop(seconds=30)
async def foo():
    members = bot.get_all_members()
    for member in members:
        if isinstance (member.status, discord.Status.online):
            print(member)

foo.start()

client.run(TOKEN)