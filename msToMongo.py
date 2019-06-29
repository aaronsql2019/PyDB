# -*- coding:utf-8 -*-
from datetime import datetime
from mongoConnect import mongoConnect
from msSqlConnect import msSqlConnect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pprint
import pyodbc
import re

# Connect MSSQL
cnxn = msSqlConnect()
# Create a cursor from the connection
cursor = cnxn.cursor()

# Connect MongoDB
client = mongoConnect()
# get Collection
boxes = client.test.boxes
# Delete existing data
boxes.delete_many({})

print('\nMSSQL的資料-----')
try:
    # Read the rows one at a time
    for row in cursor.execute("SELECT * FROM Boxes"):
        print('%-17s %-28s %s' % (row.Name, row.Size, row.Colored))

        # Parsing Length, Width, Height
        # Compile a pattern to capture float values
        length = float(re.findall(r'\d+\.?\d+', row.Size)[0])
        width = float(re.findall(r'\d+\.?\d+', row.Size)[1])
        height = float(re.findall(r'\d+\.?\d+', row.Size)[2])
        print('字串轉換成浮點數: ', length, width, height)

        # Insert to MongoDB
        box = {"Name": row.Name,
               "Length": length,
               "Width": width,
               "Height": height,
               "Colored": row.Colored}
        # pprint.pprint(box)
        boxes.insert_one(box)
except:
    print("MSSQL data not parsed, and didn't insert to MongoDB!!")

print('\nMongoDB的資料-----')
# Read more
for abox in boxes.find({}):
    pprint.pprint(abox)
# count
print("總共從MSSQL輸入了", boxes.count_documents({}), "種箱子")
