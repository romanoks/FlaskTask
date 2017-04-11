import flask
from flask_restful import abort, Resource, reqparse
import WhitelistData

class AllWhiteList(Resource):
    def get(self):
        # print(application.db)
        print('AllWhitelist')
        return WhitelistData, 201
