from flask import Flask
from flask_restful import Resource, Api, reqparse
from pymongo import ALL,MongoClient
import ast
from bson.json_util import dumps
from bson.json_util import loads

app = Flask(__name__)
api = Api(app)

class Name(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['attractionDatabase']
        collection = db['attractions']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return loads(dumps(retrieved)), 200

    def post(self):
        pass

api.add_resource(Name, '/name')

if __name__ == '__main__':
    app.run()