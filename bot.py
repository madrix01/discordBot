import discord
from discord.ext import commands
from cmd import cmd, cmd_init

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
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to TestServer69 {member.mention} """)



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
        print('1', lst)
        a = listToString(lst[1:])
        post_data = {
                'message' : a 
            }
        print('2', a)

        if lst[0][1:] in cmd["msg"].keys():

            await message.channel.send(message_cmd(message)[lst[0][1:]])
        
        if lst[0][1:] in cmd['db'].keys():
            db_cmd(post_data)
            await message.channel.send("saved!😁")
        else:
            await message.channel.send("Enter a valid command")
            

client.run(tokenKey)
   