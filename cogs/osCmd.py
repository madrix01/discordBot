import discord
from discord.ext import commands
import os
from cmd import num_lines, read_lines, write_path, git_push
import webbrowser


pathFile = "folderpath.txt"

class osCmd(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #commands

    #opens a file in explorer in your computer
    @commands.command(aliases=['e'])
    async def explorer(self ,ctx, folder = ""):
        os.startfile(f'C:/madrix/{folder}')
        await ctx.channel.purge(limit=1)
    
    #open cmd <your cmd>
    @commands.command()
    async def cmd(self, ctx, cmd=""):
        os.system(f"start /B start cmd.exe @cmd /k {cmd}")
        await ctx.channel.purge(limit=1)
    
    #add git initialised folder path
    @commands.command(pass_context=True, aliases=["ap"])
    async def addpath(self, ctx, *path):
        path = list(path)
        y = " "
        path = y.join(path)
        if path == "":
            await ctx.channel.send("It's empty like your brain")
        else:
            write_path(path, pathFile)
            await ctx.channel.send(f"{path} Saved!")

    #view all the git path
    @commands.command(aliases=['gp'])
    async def gitpath(self, ctx):
        gplist = []
        gps = ""
        for i in range(num_lines(pathFile)):
            gplist.append(f"{i} {read_lines(i, pathFile)}")
            gps = "\n".join(gplist)
        em = discord.Embed(title="Git paths" , description=gps, colour=0xFF8300)
        await ctx.send(embed=em)
    
    #git push >git <path no from gp> <commit message>
    @commands.command()
    async def git(self, ctx, pthNo, *commitMessage):
        commitMessage = list(commitMessage)
        y = " "
        commitMessage = y.join(commitMessage) 
        pthNo = int(pthNo)
        if pthNo > num_lines(pathFile):
            await ctx.channel.send("Enter proper path no.") 
        else:
            pth = str(read_lines(pthNo, pathFile))
            commitMessage = str(commitMessage)
            git_push(pth, commitMessage)
            await ctx.channel.send(f"Commited {commitMessage} to master branch ")


    #open browser and searches word
    @commands.command(pass_context=True)
    async def s(self, ctx, *search):
        search = list(search)
        y = " "
        search = y.join(search)
        url = "https://www.google.com.tr/search?q={}".format(search)
        webbrowser.open_new_tab(url)
        print("Directing to new page")
    
    #opens url in new windows 
    @commands.command(pass_context=True)
    async def url(self, ctx, url):
        webbrowser.open_new_tab(url)
        print("Directing to new page")


def setup(client):
    client.add_cog(osCmd(client))
