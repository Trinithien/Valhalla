# bot.py
import os
import sched, time
import board
import neopixel
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
s = sched.scheduler(time.time, time.sleep)

pixels = neopixel.NeoPixel(board.D21, 120, brightness=0.2)

def check_online(sc):
    # Henter alle medlemene den har tilgang til.
    members = client.get_all_members()
    # For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        # Hvis statusen per medlem er det samme som status online printer vi den personen.
        if member.status == discord.Status.online:
            print(member,member.status)
            if member.id == 166164767701073921:
                pixels[0]= (0,0,255)
                print('on')
            if member.id == 294969517237469185:
                pixels[2]= (0,0,255)
                print('on')
        elif member.status == discord.Status.offline:
            if member.id == 166164767701073921:
                pixels[0]= (0,0,0)
                print('off')
            if member.id == 294969517237469185:
                pixels[2]= (0,0,0)
                print('off')
            print(member,member.status)
        else:
            print(member,member.status)
            
    s.enter(5, 1, check_online, (sc,))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # Henter alle medlemene den har tilgang til.
    members = client.get_all_members()
    # For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        # Hvis statusen per medlem er det samme som status online printer vi den personen.
        
        if member.status == discord.Status.online:
            print(member,member.status)
            if member.id == 166164767701073921:
                pixels[0]= (0,0,255)
                print('on')
            if member.id == 294969517237469185:
                pixels[2]= (0,0,255)
                print('on')
        elif member.status == discord.Status.offline:
            print(member,member.status)
            if member.id == 166164767701073921:
                pixels[0]= (0,0,0)
                print('off')
            if member.id == 294969517237469185:
                pixels[2]= (0,0,0)
                print('off')
        else:
            print(member,member.status)
            
    s.enter(5, 1, check_online, (s,))
    s.run()
    
@client.event
async def on_message(message):
    print(message.author.id)

client.run(TOKEN)