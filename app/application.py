from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from resources import userResources, allWhiteLists

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api = Api(app)

db = SQLAlchemy(app)

api.add_resource(userResources.HelloWorld, '/')
api.add_resource(allWhiteLists.AllWhiteList, '/whitelist')

if __name__ == '__main__':
    app.run(debug=True)
    # main()
