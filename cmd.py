from pymongo import MongoClient
from db import save_data

client = MongoClient('mongodb://localhost:27017')



cmd_init = "."

info = f"""
Hello I am Dokkaebi, I am a bot created by Madrix.
Type '{cmd_init}' in front of command to activate.
commands-
.help : All the info
.hello : Greets
.create <message> : Save message to the datatbase
"""


def message_cmd(x):
    return f"Hi {x.author}"



cmdList = {
    "msg" : {
        'help' : info,
        'hello' : message_cmd
    },
    "db" : {
        'create' : save_data
    }
}





