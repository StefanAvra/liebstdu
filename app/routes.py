from app import app, db
from flask import render_template, request, session
from random import randint
from datetime import datetime
from app.models import User, Thing, Vote
from sqlalchemy.sql.expression import func, select
import names


@app.route("/")
def index():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        if user:
            # success
            pass
        else:
            session.pop(user_id, None)
    else:
        u = User(name=names.get_full_name())
        db.session.add(u)
        db.session.commit()
        session["user_id"] = u.id
        session.permanent = True
    row_count = Thing.query.count()
    thing = Thing.query.offset(randint(0, row_count - 1)).first()
    return {"id": thing.id, "name": thing.name, "plural": thing.plural}


@app.route("/things/")
@app.route("/things/<p_thing>/")
def get_things(p_thing=None):
    t = {}
    if not p_thing:
        for thing in Thing.query.all():
            t[thing.id] = {"name": thing.name, "plural": thing.plural}
        return t
    else:
        thing = Thing.query.filter(Thing.name.ilike(p_thing)).first()
    try:
        t = {"id": thing.id, "name": thing.name, "plural": thing.plural}
    except:
        t = f"no thing {p_thing} found"

    return t


@app.route("/votes/")
def get_votes():
    votes = {}
    for vote in Vote.query.all():
        votes[vote.id] = {
            "thing_id": vote.thing_id,
            "user_id": vote.user_id,
            "vote_love": vote.vote_love,
            "vote_hobby": vote.vote_hobby,
            "timestamp": vote.timestamp,
        }
    return votes


@app.route("/votes/<p_thing>/", methods=["GET", "POST"])
def vote(p_thing=None):
    if request.method == "GET":
        votes = {}
        thing = Thing.query.filter(Thing.name.ilike(p_thing)).first()
        if not thing:
            return f"no thing '{p_thing}'", 404

        for vote in Vote.query.filter(Vote.thing_id == thing.id).all():
            votes[vote.id] = {
                "thing_id": vote.thing_id,
                "user_id": vote.user_id,
                "vote_love": vote.vote_love,
                "vote_hobby": vote.vote_hobby,
                "timestamp": vote.timestamp,
            }
        return votes

    if request.method == "POST":
        user_id = session.get("user_id")
        if user_id:
            user = User.query.get(user_id)
            if user:
                # success
                pass
            else:
                return "no user", 400
        else:
            return "no user", 400
            
        thing = Thing.query.filter(Thing.name.ilike(p_thing)).first()
        if not thing:
            return f"no thing '{p_thing}'", 400

        vote_love = int(request.form.get("vote_love"))
        vote_hobby = int(request.form.get("vote_hobby"))
        thing_id = thing.id
        timestamp = datetime.utcnow()

        if vote_love not in [0, 1]:
            return f"vote_love cannot be {vote_love}", 400

        if vote_hobby not in [0, 1]:
            return f"vote_hobby cannot be {vote_hobby}", 400

        if vote_love == 0 and vote_hobby == 1:
            return f"no hobby if you do not love it, ok?!", 400

        v = Vote.query.filter(
            Vote.thing_id == thing_id, Vote.user_id == user_id
        ).first()
        if not v:
            v = Vote()
        v.user_id = user_id
        v.thing_id = thing_id
        v.vote_love = vote_love
        v.vote_hobby = vote_hobby
        v.timestamp = timestamp

        db.session.add(v)
        db.session.commit()

        return "succesful"

