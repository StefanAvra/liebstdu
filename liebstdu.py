from app import app, db
from app.models import User, Thing, Vote
from flask import session
import sys


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Thing': Thing, 'Vote': Vote}


@app.before_request
def check_user_session():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        print(f'user {user.name} logged', file=sys.stdout)
        if not user:
            session.pop(user_id, None)
    else:
        u = User(name=names.get_full_name())
        db.session.add(u)
        db.session.commit()
        session["user_id"] = u.id
        session.permanent = True
        print(f'user {u.name} created', file=sys.stdout)

# helper function I used to init default values manually. todo: add to models?
def init_default_things():
    things = [
        ('Fun', 0),
        ('Wurst', 0),
        ('Pizza', 0),
        ('Abli', 0),
        ('Sex', 0),
        ('Babes', 1),
        ('Maultaschen', 1),
        ('schlafen', 0),
        ('Essen', 0),
        ('Dreads', 1),
        ('Sonne', 0),
        ('Japan', 0),
        ('Bolognese', 0),
        ('Tee', 0),
        ('Kaffee', 0),
        ('Spiele', 1),
        ('Bärlauch', 0),
        ('Pflanzen', 1),
        ('Dua Lipa', 0),
        ('Wasser', 0),
        ('Video Spiele', 1),
    ]
    for thing in things:
        t = Thing(name=thing[0], plural=thing[1])
        db.session.add(t)
        db.session.commit()
