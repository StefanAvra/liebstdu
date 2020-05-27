from app import db

class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Thing {}>'.format(self.name)
