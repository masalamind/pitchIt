from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from . import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(255))

    votes = db.relationship('Vote', backref='user')
    pitches = db.relationship('Pitch', backref='user')
    bookmarks = db.relationship('Bookmark', backref='user')

    def __repr__(self):
        return f'User {self.username}'

class PitchCategory(db.Model):
    __tablename__ = 'pitch_categories'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(140))

    pitches = db.relationship('Pitch', backref='pitch_category')

class Pitch(db.Model):
    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer, primary_key=True)
    publish_date = db.Column(db.DateTime)
    pitch_creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    pitch_category_id = db.Column(db.Integer, db.ForeignKey('pitch_categories.category_id'))

    comments = db.relationship('Comment', backref='pitch_id')

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
    user_id = db.Column(db.Integer)
    comment_time = db.Column(db.DateTime)

class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    bookmark_id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class Vote(db.Model):
    __tablename__ = 'votes'

    vote_id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Boolean)
    downvote = db.Column(db.Boolean)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
    voter_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))



# db.create_all()