import discord
from discord.ext import commands


client = commands.Bot(command_prefix="|")


@client.event
async def on_ready():
    print("Ayy Ayy madrix")


@client.event
async def on_member_join(member):
    print(f'{member} has joined')


@client.event
async def on_member_remove(member):
    print(f'bye bye {member}')

@client.command()
async def ping(ctx):
    await ctx.send("chup bsdk")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    y = message.content 
    if y[0] == "/":
        y = message.content
        z = y[1:]
        print(z)
        try:
            z = float(z)
            z = z + 1
            await message.channel.send(z)
        except:
            response = "Pls enter valid no."
            await message.channel.send(response)


client.run('NjgzMTc2MDUxNzczNDA3Mjgy.XlnvYA.XHguSi_ALEqjdKVTPnU5rQgv1I8')
