# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from mongoConnect import mongoConnect
from datetime import datetime
from datetime import timedelta
import pprint
import schedule
import time

client = mongoConnect()

# get Database
db = client.test
# get Collection
posts = db.posts


def insertJob():
    print("自動張貼文章...", datetime.now())
    # Create
    post = {"author": "Robot",
            "text": "My blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.utcnow()}
    posts.insert_one(post)


def deleteJob():
    total = posts.count_documents({})
    print("總共", total, "則貼文")
    # Delete posts over n hours
    deleted = posts.delete_many(
        {'date': {'$lt': datetime.utcnow() - timedelta(minutes=3)}})
    print("自動清除過期文章", deleted.deleted_count, "則")


# auto post every 20 seconds
schedule.every(20).seconds.do(insertJob)
# auto delete post every 3 minutes
schedule.every(3).minutes.do(deleteJob)

while True:
    schedule.run_pending()
    time.sleep(1)
