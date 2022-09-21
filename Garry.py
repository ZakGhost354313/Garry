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
    # no
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
        # this command is for me to use as a template
        #response = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c"
        test1 = f'''
            \\x00 - \x00
            \\x01 - \x01
            \\x02 - \x02
            \\x03 - \x03
            \\x04 - \x04
            \\x05 - \x05
            \\x06 - \x06
            \\x07 - \x07
            \\x08 - \x08
            \\x09 - \x09
            \\x0a - \x0a
            \\x0b - \x0b
            \\x0c - \x0c
            \\x0d - \x0d
            \\x0e - \x0e
            \\x0f - \x0f
            \\x10 - \x10
            \\x11 - \x11
            \\x12 - \x12
            \\x13 - \x13
            \\x14 - \x14
            \\x15 - \x15
            \\x16 - \x16
            \\x17 - \x17
            \\x18 - \x18
            \\x19 - \x19
            \\x1a - \x1a
            \\x1b - \x1b
            \\x1c - \x1c
            \\x1d - \x1d
            \\x1e - \x1e
            \\x1f - \x1f
            \\x20 - \x20
            \\x21 - \x21
            \\x22 - \x22
            \\x23 - \x23
            \\x24 - \x24
            \\x25 - \x25
            \\x26 - \x26
            \\x27 - \x27
            \\x28 - \x28
            \\x29 - \x29
            \\x2a - \x2a
            \\x2b - \x2b
            \\x2c - \x2c
            \\x2d - \x2d
            \\x2e - \x2e
            \\x2f - \x2f
'''
        test2 = f'''
            \t\\x30 - \x30
            \\x31 - \x31
            \\x32 - \x32
            \\x33 - \x33
            \\x34 - \x34
            \\x35 - \x35
            \\x36 - \x36
            \\x37 - \x37
            \\x38 - \x38
            \\x39 - \x39
            \\x3a - \x3a
            \\x3b - \x3b
            \\x3c - \x3c
            \\x3d - \x3d
            \\x3e - \x3e
            \\x3f - \x3f
            \\x40 - \x40
            \\x41 - \x41
            \\x42 - \x42
            \\x43 - \x43
            \\x44 - \x44
            \\x45 - \x45
            \\x46 - \x46
            \\x47 - \x47
            \\x48 - \x48
            \\x49 - \x49
            \\x4a - \x4a
            \\x4b - \x4b
            \\x4c - \x4c
            \\x4d - \x4d
            \\x4e - \x4e
            \\x4f - \x4f
            \\x50 - \x50
            \\x51 - \x51
            \\x52 - \x52
            \\x53 - \x53
            \\x54 - \x54
            \\x55 - \x55
            \\x56 - \x56
            \\x57 - \x57
            \\x58 - \x58
            \\x59 - \x59
            \\x5a - \x5a
            \\x5b - \x5b
            \\x5c - \x5c
            \\x5d - \x5d
            \\x5e - \x5e
            \\x5f - \x5f
            \\x60 - \x60
            \\x61 - \x61
            \\x62 - \x62
            \\x63 - \x63
            \\x64 - \x64
            \\x65 - \x65
            \\x66 - \x66
            \\x67 - \x67
            \\x68 - \x68
            \\x69 - \x69 noice
            \\x6a - \x6a
            \\x6b - \x6b
            \\x6c - \x6c
            \\x6d - \x6d
        '''
        test3 = f'''\t\\x6e - \x6e
            \\x6f - \x6f
            \\x70 - \x70
            \\x71 - \x71
            \\x72 - \x72
            \\x73 - \x73
            \\x74 - \x74
            \\x75 - \x75
            \\x76 - \x76
            \\x77 - \x77
            \\x78 - \x78
            \\x79 - \x79
            \\x7a - \x7a
            \\x7b - \x7b
            \\x7c - \x7c
            \\x7d - \x7d
            \\x7e - \x7e
            \\x7f - \x7f
            \\x80 - \x80
            \\x81 - \x81
            \\x82 - \x82
            \\x83 - \x83
            \\x84 - \x84
            \\x85 - \x85
            \\x86 - \x86
            \\x87 - \x87
            \\x88 - \x88
            \\x89 - \x89
            \\x8a - \x8a
            \\x8b - \x8b
            \\x8c - \x8c
            \\x8d - \x8d
            \\x8e - \x8e
            \\x8f - \x8f
            \\x90 - \x90
            \\x91 - \x91
            \\x92 - \x92
            \\x93 - \x93
            \\x94 - \x94
            \\x95 - \x95
            \\x96 - \x96
            \\x97 - \x97
            \\x98 - \x98
            \\x99 - \x99
            \\x9a - \x9a
            \\x9b - \x9b
            \\x9c - \x9c
            \\x9d - \x9d
            \\x9e - \x9e
            \\x9f - \x9f
        '''
        test4 = f'''\\xa0 - \xa0
            \\xa1 - \xa1
            \\xa2 - \xa2
            \\xa3 - \xa3
            \\xa4 - \xa4
            \\xa5 - \xa5
            \\xa6 - \xa6
            \\xa7 - \xa7
            \\xa8 - \xa8
            \\xa9 - \xa9
            \\xaa - \xaa
            \\xab - \xab
            \\xac - \xac
            \\xad - \xad
            \\xae - \xae
            \\xaf - \xaf
            \\xb0 - \xb0
            \\xb1 - \xb1
            \\xb2 - \xb2
            \\xb3 - \xb3
            \\xb4 - \xb4
            \\xb5 - \xb5
            \\xb6 - \xb6
            \\xb7 - \xb7
            \\xb8 - \xb8
            \\xb9 - \xb9
            \\xba - \xba
            \\xbb - \xbb
            \\xbc - \xbc
            \\xbd - \xbd
            \\xbe - \xbe
            \\xbf - \xbf
            \\xc0 - \xc0
            \\xc1 - \xc1
            \\xc2 - \xc2
            \\xc3 - \xc3
        '''
        test5 = f'''\\xc4 - \xc4
            \\xc5 - \xc5
            \\xc6 - \xc6
            \\xc7 - \xc7
            \\xc8 - \xc8
            \\xc9 - \xc9
            \\xca - \xca
            \\xcb - \xcb
            \\xcc - \xcc
            \\xcd - \xcd
            \\xce - \xce
            \\xcf - \xcf
            \\xd0 - \xd0
            \\xd1 - \xd1
            \\xd2 - \xd2
            \\xd3 - \xd3
            \\xd4 - \xd4
            \\xd5 - \xd5
            \\xd6 - \xd6
            \\xd7 - \xd7
            \\xd8 - \xd8
            \\xd9 - \xd9
            \\xda - \xda
            \\xdb - \xdb
            \\xdc - \xdc
            \\xdd - \xdd
            \\xde - \xde
            \\xdf - \xdf
        '''
        await message.channel.send(test1)
        await message.channel.send(test2)
        await message.channel.send(test3)
        await message.channel.send(test4)
        await message.channel.send(test5)
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
        response = f'''Garry.py the bestest discord bot
        \x60{prefix}help\x60 gives you this message in return
        \x60{prefix}lol\x60 gives you a funny meme, unless of course you have really bad luck...
        \x60{prefix}ping\x60 pong
        \x60{prefix}idk\x60 simply a funny joke, it messages back \"really\"
        '''
        print(response)
        await message.channel.send(response)
    elif cmd == f'{prefix}t':
        if thing[1] == "est":
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

client.run(TOKEN)
