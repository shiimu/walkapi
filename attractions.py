import pymongo
from pymongo import ALL, MongoClient

def retrieveData():
    client = MongoClient('localhost', 27017)
    db = client['attractionDatabase']
    collection = db['attractions']

    retrieved = collection.find({})
    for names in retrieved:
        print(names)

