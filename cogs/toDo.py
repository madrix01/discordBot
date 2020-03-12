import discord
from discord.ext import commands
import os
from pymongo import MongoClient

class toDo(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    


    #commands
    @commands.command()
    async def task(self, ctx, task, status):
        clientdb = MongoClient("mongodb://localhost:27017")
        db = clientdb['todo']
        posts = db.posts
        task = task.lower()
        post_data = {
            'title': task,
            'status': status,
            'author': ctx.author.name
        }
        result = posts.insert_one(post_data)
        await ctx.channel.send("Done bitch!")
    
    
    @commands.command()
    async def td(self, ctx, status):
        clientdb = MongoClient("mongodb://localhost:27017")
        db = clientdb['todo']
        posts = db.posts
        if status == "1":
            c = []
            for y in posts.find():
                if y["status"] == "1":
                    c.append(y['title'])
            for x in range(len(c)):
                tdc = "\n".join(c)
            em = discord.Embed(title="Completed Tasks" , description=tdc, colour=0x00FF04)
            await ctx.channel.send(embed=em)
        if status == "0":
            ic = []
            for y in posts.find():
                if y["status"] == "0":
                    ic.append(y['title'])
            for x in range(len(ic)):
                tdic = "\n".join(ic)
            em = discord.Embed(title="Remaining Tasks" , description=tdic, colour=0xFF0000)
            await ctx.channel.send(embed=em)
                
                


    @commands.command()
    async def i(self, ctx, title):
        clientdb = MongoClient("mongodb://localhost:27017")
        db = clientdb['todo']
        posts = db.posts
        for i in posts.find():
            if i["title"] == title:
                myquery = {'title':title}
                newvalues = { "$set": { "status": "1" } }
                posts.update_one(myquery, newvalues)
                print("done")

    @commands.command()
    async def o(self, ctx, title):
        clientdb = MongoClient("mongodb://localhost:27017")
        db = clientdb['todo']
        posts = db.posts
        for i in posts.find():
            if i["title"] == title:
                myquery = {'title':title}
                newvalues = { "$set": { "status": "0" } }
                posts.update_one(myquery, newvalues)
                print("done")

            


def setup(client):
    client.add_cog(toDo(client))