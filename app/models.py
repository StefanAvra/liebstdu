from datetime import datetime
from app import db

class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    plural = db.Column(db.Integer)
    votes = db.relationship('Vote', backref='thing')

    def __repr__(self):
        return '<Thing {}>'.format(self.name)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    votes = db.relationship('Vote', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thing_id = db.Column(db.Integer, db.ForeignKey('thing.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vote_love = db.Column(db.Integer)
    vote_hobby = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Vote {} by {}>'.format(self.id, self.user_id)
