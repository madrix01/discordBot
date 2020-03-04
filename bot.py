import discord
from discord.ext import commands, tasks
from cmd import info, check_role
import random
from gifs import search_gif



def read_token(c):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[c].strip()

tokenKey = read_token(0)

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
async def roll(ctx, value):
    x = random.choice([1, 2, 3, 4, 5, 6])
    if value == str(x):
        em = discord.Embed(title="You Won" , description=f"Your No.> {value}\nSecret No.> {x}", colour=0x00FF00)
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title="You Lose" , description=f"""Your No.> {value}\nSecret No.> {x}""", colour=0xFF0000)
        await ctx.send(embed=em)
    
@client.command()
async def gif(ctx, query='what'):
    gif = await search_gif(query)
    await ctx.send('Gif URL : ' + gif)



client.run(tokenKey)
