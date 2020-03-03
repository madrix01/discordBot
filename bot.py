import discord
from discord.ext import commands, tasks
from cmd import info


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

tokenKey = read_token()

id = 683190065488199690
client = commands.Bot(command_prefix="!")
client.remove_command("help")
#client = discord.Client()
bot_id = "<@683176051773407282>"

def listToString(s):
    str1 = " "    
    return str1.join(s)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with feelings"))
    print("Ayy Ayy captain")



@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Type "!help" to see all the commands'
    )

@client.event
async def on_member_remove(member):
    print(f'bye bye {member}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Pls give proper commands")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No Command found, Type '!help' to get all commands")



@client.command()
async def hello(ctx):
    await ctx.send(f"Hii {ctx.message.author} {ctx.message.author.role}")


@client.command()
async def help(ctx):
    await ctx.send(f"Hii {ctx.message.author} {info}")


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)









client.run(tokenKey)
   