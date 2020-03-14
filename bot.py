import discord
from discord.ext import commands, tasks
from cmd import info, check_role
import random
from gifs import search_gif
from cmd import *
import os
import asyncio


tokenKey = read_lines(0, "token.txt")

id = 683190065488199690
client = commands.Bot(command_prefix=">")
client.remove_command("help")
#client = discord.Client()
bot_id = "<@683176051773407282>"

def listToString(s):
    str1 = " "    
    return str1.join(s)


async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='683190065488199697')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(20) 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with Madrix's Code"))
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

"""@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Pls give proper commands")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No Command found, Type '!help' to get all commands")"""


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def r(ctx, extension = "gitpy"):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    print("reload")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hii {ctx.message.author} ")


@client.command()
async def help(ctx):
    em = discord.Embed(title="You Won" , description=info, colour=0xFF8300)
    await ctx.send(embed=em)


@client.command()
@commands.has_role('Developer')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(pass_context=True)
async def roles(ctx):
    x = ctx.message.author.roles
    rls = ""
    x = x[1:]
    for i in range(len(x)):
        rls = rls + " " + str(x[i])
    await ctx.send(rls)


@client.command()
async def gif(ctx, query='what'):
    gif = await search_gif(query)
    await ctx.send('Gif URL : ' + gif)



@client.command()
async def d(ctx):
    await ctx.send(f"{tdc} {tdic}")



for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.loop.create_task(my_background_task())
client.run(tokenKey)
     