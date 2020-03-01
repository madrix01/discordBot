import discord
from discord.ext import commands
from cmd import cmdList, cmd_init
from tokenki import tokenKey
from pymongo import MongoClient


id = 683190065488199690
#client = commands.Bot(command_prefix="#")
client = discord.Client()
bot_id = "<@683176051773407282>"

def listToString(s):
    str1 = " "    
    return str1.join(s)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Type ".help" to see all the commands'
    )


@client.event
async def on_member_remove(member):
    print(f'bye bye {member}')

@client.event
async def on_message(message):
    id = client.get_guild(683190065488199690)
    channels = ['command']
    msg = str(message.content)
    print(msg)
    
    if msg[0] == cmd_init:
        lst = msg.split()
        inCmdBody = listToString(lst[1:])
        print(inCmdBody)
        inCmd = lst[0][1:]
        if inCmd in cmdList['msg'].keys():
            if inCmd == "hello":
                await message.channel.send(cmdList['msg'][inCmd](message))
            else:
                await message.channel.send(cmdList["msg"][inCmd])
        elif inCmd in cmdList['db'].keys():
            if inCmd == "create":
                if inCmdBody != "":
                    post = {
                        'message' : inCmdBody
                    }
                    cmdList['db']["create"](post)
                    await message.channel.send("Saved! ;)")
                else:
                    await message.channel.send("Can't save blank message!")
        else:
            await message.channel.send("Pls enter a valid command! Type '.help' for all the commnads")


client.run(tokenKey)
   