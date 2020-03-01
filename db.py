from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017')
db = client['bot_data']
posts = db.posts


def save_data(ms):
    posts.insert_one(ms)