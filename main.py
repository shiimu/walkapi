from flask import Flask
from flask_restful import Resource, Api, reqparse
from pymongo import ALL,MongoClient
import ast


app = Flask(__name__)
api = Api(app)

class Name(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['attractionDatabase']
        collection = db['attractions']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
        return 401
    
    def put(self):
        return 401

    def delete(self):
        return 401

    def push(self):
        return 401

api.add_resource(Name, '/name')


if __name__ == '__main__':
    app.run()