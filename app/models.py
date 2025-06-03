from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    points = db.Column(db.Integer)
    matches_played = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    players = db.relationship('Player', backref='team')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    position = db.Column(db.String(30))
    rating = db.Column(db.Float)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
