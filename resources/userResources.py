import flask
from flask_restful import abort, Resource, reqparse

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'Hello World!!'}
