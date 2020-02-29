from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')



cmd_init = "."

info = f"""
Hello I am Dokkaebi, I am a bot created by Madrix.
Type '{cmd_init}' in front of command to activate.
commands-
.help : All the info
.hello : Greets
.avengers : See avengers movie
.time : current time
"""


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def cmd(x, a):

    def save_data(ms):
        db = client['bot_data']
        posts = db.posts
        posts.insert_one(ms)
        return "saved!😁" 
        
    post_data = {
        'message' : a 
    }
    cmd = {
        'help' : info,
        'hello' : f"Hi {x.author}!",
        'time' : current_time,
        'create' : save_data(post_data)
    }
    return cmd



    def todo():
        td_cmd = {
            'create'
        } 