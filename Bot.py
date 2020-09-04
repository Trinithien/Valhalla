# bot.py
import os
import sched, time
import board
from threading import Timer
import neopixel
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
pixels = neopixel.NeoPixel(board.D21, 120, brightness=0.2)

def check_online():
    # Henter alle medlemene den har tilgang til.
    members = client.get_all_members()
    # For hver member i arrayet (noe med flere elementer) members hentet ovenfra.
    for member in members:
        # Hvis statusen per medlem er det samme som status online printer vi den personen.
        if member.status == discord.Status.online:
            print(member,member.status)
            if member.id == 166164767701073921: #Tobi
                pixels[0]= (0,0,255)
                print('on')
            if member.id == 294969517237469185: #Turbo
                pixels[2]= (0,0,255)
                print('on')
            if member.id == 164089595938471936: #Quinn
                for i in range(3,100):
                    pixels[i]= (255,255,0)
                    time.sleep(1/1000)
        elif member.status == discord.Status.offline:
            if member.id == 166164767701073921: #Tobi
                pixels[0]= (0,0,0)
                print('off')
            if member.id == 294969517237469185: #Turbo
                pixels[2]= (0,0,0)
                print('off')
            if member.id == 164089595938471936: #Quinn
                for i in range(3,100):
                    pixels[i]= (0,0,0)
                    time.sleep(1/1000)
            print(member,member.status)
        else:
            print(member,member.status)
    Timer(10.0,check_online).start() # Method calls itself again after 60 seconds

            
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    check_online() # Call method once

@client.event
async def on_message(message):
    print(message.author.id)


client.run(TOKEN)
