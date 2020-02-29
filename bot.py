import discord
from discord.ext import commands
from cmd import cmd, cmd_init

id = 683190065488199690
#client = commands.Bot(command_prefix="#")
client = discord.Client()
bot_id = "<@683176051773407282>"

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
        msg = msg[1:]
        if msg in cmd(message).keys():
            await message.channel.send(cmd(message)[msg])
        else:
            await message.channel.send("Enter a valid command")
            

client.run('NjgzMTc2MDUxNzczNDA3Mjgy.XlpqXQ.Mx0McbZYNKV4y5CHD_Jh2eUGySs')
   