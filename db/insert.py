#coding:utf-8


"""The News Insert Implementation."""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def insert_news(date, title, html, trhtml, text, trtext):
    client = MongoClient(connectTimeoutMS=2000, serverSelectionTimeoutMS=2000)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")
        return

    db = client.news
    coll = db[date]

    post = {"title": title,
            "text": text,
            "trtext": trtext,
            "html": html,
            "trhtml": trhtml,
            # "date": datetime.datetime.utcnow()
        }
    coll.insert_one(post)
