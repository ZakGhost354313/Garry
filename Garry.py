#!/usr/bin/env python
from http.client import ResponseNotReady
import os
from time import sleep
import random
import sys
import json
from types import SimpleNamespace
from xmlrpc.client import ResponseError
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

file = open("./memegen.json")
data_set = file.read()
data = json.loads(data_set, object_hook=lambda d: SimpleNamespace(**d))
file.close()

def beemoviescript():
    with open("./beemovie.txt") as file:
        data = file.read()
    scriptlines = data.splitlines()
    return scriptlines

def getMeme():
    i = random.randint(0, 191)
    id = data[i].id
    example = data[i].example.text[1]
    url = 'https://api.memegen.link/images/'+id+'/high_quality/'+example
    return url

brooklyn_99_quotes = [
    'I\'m the human form of the 💯 emoji.',
    'Bingpot!',
    (
        'Cool. Cool cool cool cool cool cool cool, '
        'no doubt no doubt no doubt no doubt.'
    ),
]

def getMemesTXT():
    with open("./memes.txt") as file:
        data = file.read().splitlines()
    return data
imgur_memes = getMemesTXT()

def getHexTXT():
    with open("./hex.txt") as file:
        data = file.read().splitlines()
    return data

def getHelpTXT():
    with open("./help.txt") as file:
        data = file.read()
    return data

client = discord.Client(intents=discord.Intents(
    messages=True, members=True, message_content=True))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
async def on_member_leave(member):
    await member.create_dm()
    await member.dm_channel.send(f'{member.name}!! you\'d better have left for a good reason, if this was an accident you can always dm GhostKiller7724#3863')
prefix = "~"


channel_id_switch = {
    #my channel ids/names for my server "idk"
    1015448557966340237:"bot-testing",
    1021142868393472092:"hydra-song-requests",
    1015452158658891786:"text-vc",
    864537239018799138:"general",
    1015448735897092246:"memes",
    1015450029240107019:"bot",
    1015452602286219274:"rules",
    1015454195970736198:"afk",
    1015455622478692422:"spam",
    1016027754459828244:"roles",
    1020494043471413279:"counting",
    1021567482525401149:"hydra-text-vc"
}
def channel_id_switch_(id):
    return channel_id_switch.get(id,"invalid/unknown id")

@client.event
async def on_message(message):
    print(message)
    channel_name = channel_id_switch_(message.channel.id)
    print(f'channel:\t{channel_name}\nauthor:\t{message.author}\nmessage:\t{message.content}\n')
    if message.author == client.user:
        return
#    if message.content != None:
#        response = f'full name:{message.author}\nname:{message.author.name}\nnickname:{message.author.nick}\n\n{message}\n\n{client.event}'
#        await message.channel.send(response)
#
#        print(message)
#        print(response)
    thing = message.content.split(' ')
    cmd = thing[0]
    if cmd == f'{prefix}end':
        print('\n\n\texiting on bot command\n\n\n')
        response = 'exiting...'
        await message.channel.send(response)
        if message.author.discriminator == '3863':#my specific user number
            print('exiting...')
            exit(0)
        elif message.author.discriminator == '7815':#my friend's specific user number
            print('exiting...')
            exit(0)
        else:
            print('someone tried to exit')
            response = "lol jk"
            await message.channel.send(response)
    elif cmd == f'{prefix}exit':
        print('\n\n\texiting on bot command\n\n\n')
        response = 'exiting...'
        await message.channel.send(response)
        if message.author.discriminator == '3863':#my specific user number
            print('exiting...')
            exit(0)
        elif message.author.discriminator == '7815':#my friend's specific user number
            print('exiting...')
            exit(0)
        else:
            print('someone tried to exit')
            response = "lol jk"
            await message.channel.send(response)
    elif cmd == '99!':
        response = random.choice(brooklyn_99_quotes)
        print(response)
        await message.channel.send(response)
    elif cmd == f'{prefix}ping':
        print('ping received')
        response = "pong"
        await message.channel.send(response)
        print('pong sent')
    elif cmd == f'{prefix}idk':
        print('idk')
        response = "really"
        await message.channel.send(response)
    elif cmd == f'{prefix}a':
        hexTXT = getHexTXT()
        for h in hexTXT:
            sleep(1)
            response = h
            await message.channel.send(response)
    elif cmd == f'{prefix}lol':
        #response = getMeme()
        response = random.choice(imgur_memes)
        print(message)
        print("\n\n"+response)
        await message.channel.send(response)
    elif cmd == f'{prefix}github':
        print('gave discord')
        response = "https://github.com/ZakGhost354313/Garry"
        await message.channel.send(response)
    elif cmd == f'{prefix}help':
        helpTXT = getHelpTXT()
        response = helpTXT
        print(response)
        await message.channel.send(response)
    elif cmd == f'{prefix}t':
        if thing[1] == "est":
            try:
                if thing[2] == "icle":
                    if message.author.discriminator == '7815':
                        print('carl said testicle')
                        response = "really Carl"
                        await message.channel.send(response)
                    else: 
                        print('funny 6969 420')
                        response = "really, "
                        await message.channel.send(response)
            except:
                print('testing testing')
                response = "testing testing 123"
                await message.channel.send(response)
        else:
            print('welp i geuss test failed')
            response = "welp... i geuss you did something wrong"
            await message.channel.send(response)
    elif cmd == f'{prefix}w':
        response = f'@{thing[1]} {thing[2]}'
        print(response)
        await message.channel.send(response)
    elif cmd == f'{prefix}say1':
        print(f'saying {thing[1]}')
        response = thing[1]
        await message.channel.send(response)
    elif cmd == f'{prefix}lol-test':
        ah_lol = getMeme()
        print(ah_lol)
        response = ah_lol
        await message.channel.send(response)
    elif cmd == f'{prefix}beemovie':
        channel_name = channel_id_switch_(message.channel.id)
        if channel_name == "spam":
            script = beemoviescript()
            for s in script:
                sleep(1)
                response = s
                await message.channel.send(response)
        elif channel_name != "spam":
            response = "you are not in \x23spam"
            await message.channel.send(response)
    #elif cmd == f'{prefix}example':
        #response = "this is an example script"
        #await message.channel.send(response)
client.run(TOKEN)
