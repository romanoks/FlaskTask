import os

class Config(object):
    DEBUG=True
    Testing=False
    CSRF_ENABLED=True
    SQLALCHEMY_DATABASE_URL='sqlite:identifier.sqlite'
