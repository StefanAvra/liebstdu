from app import app
from flask import render_template, request
from random import randint
from app.models import User, Thing, Vote
from  sqlalchemy.sql.expression import func, select


@app.route('/')
@app.route('/<p_thing>')
def index(p_thing=None, plural=0):
    # if not thing:
    #     selector = randint(0, len(things)-1)
    #     thing = things[selector][0]
    #     plural = things[selector][1]
    #     thing = thing.capitalize()
    # return render_template('index.html', thing=thing, plural=plural)
    if not p_thing:
        rowCount = Thing.query.count()
        thing = Thing.query.offset(randint(0, rowCount-1)).first()
    else:
        thing = Thing.query.filter(Thing.name.ilike(p_thing)).first()
    try:
        t = {'id': thing.id, 'name': thing.name, 'plural': thing.plural}
    except:
        t = 'no thing {} found'.format(p_thing)
        
    return t

@app.route('/things')
def get_things():
    all_things = {}
    for thing in Thing.query.all():
        all_things[thing.id] = {'name': thing.name, 'plural': thing.plural}
    return all_things

