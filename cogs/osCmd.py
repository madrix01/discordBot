import discord
from discord.ext import commands
import os
from cmd import num_lines, read_lines, write_path


pathFile = "folderpath.txt"

class osCmd(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #commands
    @commands.command()
    async def explorer(self ,ctx, folder = ""):
        os.startfile(f'C:/madrix/{folder}')
        await ctx.channel.purge(limit=1)
    
    @commands.command()
    async def cmd(self, ctx, cmd=None):
        os.system(f"start /B start cmd.exe @cmd /k {cmd}")
        await ctx.channel.purge(limit=1)
    
    @commands.command(pass_context=True)
    async def addpath(self, ctx, *path):
        path = list(path)
        y = " "
        path = y.join(path)
        if path == "":
            await ctx.channel.send("It's empty like your brain")
        else:
            write_path(path, pathFile)
            await ctx.channel.send(f"{path} Saved!")

    @commands.command()
    async def gitpath(self, ctx):
        gplist = []
        gps = ""
        for i in range(num_lines(pathFile)):
            gplist.append(f"{i} {read_lines(i, pathFile)}")
            gps = "\n".join(gplist)
        em = discord.Embed(title="Git paths" , description=gps, colour=0xFF8300)
        await ctx.send(embed=em)
    
    @commands.command()
    async def git(self, ctx, pthNo, commit_name):
        pthNo = int(pthNo)
        pth = read_lines(pthNo, pathFile)
        os.system(f'start /B start cmd.exe @cmd /k  cd {pth} && git add . && git commit -m "{commit_name} && git push"')

def setup(client):
    client.add_cog(osCmd(client))
