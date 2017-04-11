from app.application import db

class WhiteList(db.Model):
    __tablename__='whitelist'

    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String)

    def __init__(self, id, command):
        self.id = id
        self.command = command

    def __repr__(self):
        return '<id {}>'.format(self.id)