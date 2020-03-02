from pymongo import MongoClient
from db import save_data

client = MongoClient('mongodb://localhost:27017')



cmd_init = "."

info = f"""
Hello I am Dokkaebi, I am a bot created by Madrix.
commands-
.helpme : All the info
.hello : Greets
.create <message> : Save message to the datatbase
"""






