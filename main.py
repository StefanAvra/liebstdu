from flask import Flask, render_template
from random import randint

app = Flask(__name__)

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
    ('Bolognese', 0)
]


@app.route('/')
@app.route('/<thing>')
def home(thing=None):
    if not thing:
        selector = randint(0, len(things)-1)
        thing = things[selector][0]
    thing = thing.capitalize()
    return render_template('index.html', thing=thing)
