#!/usr/bin/env python
from http.client import ResponseNotReady
import os
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
def getMeme():
    i = random.randint(0,191)
    id = data[i].id
    example = data[i].example.text[1]
    url = 'https://api.memegen.link/images/'+id+'/high_quality/'+example
    return id.example.url

client = discord.Client(intents=discord.Intents(messages=True, members=True,message_content=True))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
prefix = "~"
@client.event
async def on_message(message):
    if message.author == client.user:return
#    if message.content != None:
#        response = f'full name:{message.author}\nname:{message.author.name}\nnickname:{message.author.nick}\n\n{message}\n\n{client.event}'
#        await message.channel.send(response)
#     
#        print(message)

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    imgur_memes = [
        "https://i.imgur.com/T3R9crd.jpeg",
        "https://i.imgur.com/OHbKpeh.jpeg",
        "https://i.imgur.com/6BjAJ96.jpeg",
        "https://i.imgur.com/AfA4ta0.jpeg",
        "https://i.imgur.com/CPt6d7u.jpeg",
        "https://i.imgur.com/Ss3y20M.jpeg",
        "https://i.imgur.com/TaXVQCR.jpeg",
        "https://i.imgur.com/6sW5Ove.jpeg",
        "https://i.imgur.com/6EYIF61.jpeg",
        "https://i.imgur.com/5ZwN91E.jpeg",
        "https://i.imgur.com/AHHk2T3.jpeg",
        "https://i.imgur.com/3t33Kir.jpeg",
        "https://i.imgur.com/gs3ydla.jpeg",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018917277921447946/3D_Saul_Goodman_sings_The_Pia_Colada_Song.mp4",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018923923666112573/Midget_Supremacists.mp4",
        #no
        "https://cdn.discordapp.com/attachments/914639440062840952/1018927838985986118/trim.42D385F3-C0AF-45E7-B713-E6D9C5A2BC1A.mov.mp4",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018927838985986118/trim.42D385F3-C0AF-45E7-B713-E6D9C5A2BC1A.mov.mp4",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018927838985986118/trim.42D385F3-C0AF-45E7-B713-E6D9C5A2BC1A.mov.mp4",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018927838985986118/trim.42D385F3-C0AF-45E7-B713-E6D9C5A2BC1A.mov.mp4",
        "https://cdn.discordapp.com/attachments/914639440062840952/1018927838985986118/trim.42D385F3-C0AF-45E7-B713-E6D9C5A2BC1A.mov.mp4",
        "no funny meme for you\n\nonly sadness",

        "https://cdn.discordapp.com/attachments/1015448735897092246/1020483018089037874/user2045_08ec50718048.png",
        "https://cdn.discordapp.com/attachments/832984821617786901/1019341996852256849/8b4f80b573c3b7925ef2e507461c6bc5.mp4",
        "https://api.memegen.link/images/ds/small_file/high_quality.png",
        "https://media.discordapp.net/attachments/680487739078213779/1020230133069656095/unknown.png?width=473&height=473",
        "https://cdn.discordapp.com/attachments/680487739078213779/1020729045169754183/unknown.png",
        "https://cdn.discordapp.com/attachments/680487739078213779/1020729113654337576/bassketbal.mp4",
        "https://cdn.discordapp.com/attachments/680487739078213779/1020850389496639528/a990f77839ae407adca0425f5abd1b02.mp4",
        "https://cdn.discordapp.com/attachments/1015448735897092246/1018350509926654022/unknown.png",
        "https://cdn.discordapp.com/attachments/1015448735897092246/1019004877734690866/unknown.png"

        
    ]
    thing = message.content.split(' ')
    cmd = thing[0]
    if cmd == f'{prefix}end':
        print('\n\n\texiting on bot command\n\n\n')
        response = 'exiting...'
        await message.channel.send(response)
        if message.author.discriminator == '3863':
            exit(0)
        else:
            response = "lol jk"
            await message.channel.send(response)
    elif cmd == f'{prefix}exit':
        print('\n\n\texiting on bot command\n\n\n')
        response = 'exiting...'
        await message.channel.send(response)
        if message.author.discriminator == '3863':
            exit(0)
        else:
            response = "lol jk"
            await message.channel.send(response)
    elif cmd == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif cmd == f'{prefix}ping':
        response = "pong"
        await message.channel.send(response)
    elif cmd == f'{prefix}idk':
        
        response = "really"
        await message.channel.send(response)
    elif cmd == f'{prefix}template':
        #this command is for me to use as a template
        response = "test \x00\x01\x02\x03"
        await message.channel.send(response)
    elif cmd == f'{prefix}lol':
        #response = getMeme()
        response = random.choice(imgur_memes)
        print(message)
        print("\n\n"+response)
        await message.channel.send(response)
    elif cmd == f'{prefix}github':
        response = "https://github.com/ZakGhost354313/Garry"
        await message.channel.send(response)
    elif cmd == f'{prefix}help':
        response = f'''Garry.py the bestest discord bot
        \x60{prefix}help\x60 gives you this message in return
        \x60{prefix}lol\x60 gives you a funny meme, unless of course you have really bad luck...
        \x60{prefix}ping\x60 pong
        \x60{prefix}idk\x60 simply a funny joke, it messages back \"really\"
        '''
        await message.channel.send(response)
    elif cmd == f'{prefix}t':
        if thing[1] == "est": 
            response = "testing testing 123"
            await message.channel.send(response)
    elif cmd == f'{prefix}w':
        response = f'@{thing[1]} {thing[2]}'
        await message.channel.send(response)

client.run(TOKEN)