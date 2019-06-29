# -*- coding:utf-8 -*-
from datetime import datetime
from mongoConnect import mongoConnect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pprint

client = mongoConnect()

# 印出所有DB的名稱
# print("MongoDB目前存在的DB有  ", client.list_database_names())
# get Database
db = client.test
print("MongoDB目前存在的collection有", db.list_collection_names())
# get Collection
posts = db.posts

# Create
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.now(),
#         "utcdate": datetime.utcnow()}
# posts.insert_one(post)

# Read one
# pprint.pprint(posts.find_one({"author": "Mike"}))
# Read more
for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)
# count
print("Mike 總共", posts.count_documents({"author": "Mike"}), "則貼文")

# Update
# posts.update_many({}, {'$addToSet': {'tags': 'updated'}})

# Read more
# for post in posts.find():
#     pprint.pprint(post)

# Delete
result = posts.delete_many({'date': {'$lt': datetime(2019, 5, 27, 11, 9)}})
# Delete all
# result = posts.delete_many({})
print("總共刪除", result.deleted_count, "則貼文")
