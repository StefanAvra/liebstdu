from app import app, db
from app.models import User, Thing, Vote

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Thing': Thing, 'Vote': Vote}

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
