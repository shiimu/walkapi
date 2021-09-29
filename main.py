from flask import Flask
from flask_restful import Resource, Api, reqparse
import pymongo
import ast

app = Flask(__name__)
api = Api(app)

class Name(Resource):
    def get(self):
        from attractions import retrieveData
        retrieveData()

    def post(self):
        pass

api.add_resource(Name, '/name')

if __name__ == '__main__':
    app.run()