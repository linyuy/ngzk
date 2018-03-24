#coding:utf-8


"""The News Insert Implementation."""

import pymongo
from pymongo import MongoClient


def insert_news(date, title, html, trhtml, text, trtext):
    client = MongoClient()
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
