# to create the database models
# we have to have 2 database, 1 for users and 1 for notes

# importing the db object defined in the __init__.py
from . import db
# custom class that we can inherit from, will give our user object something specific for flask login
from flask_login import UserMixin
# for date to be automatically added inside the notes
from sqlalchemy import func

# only for the User object we inherit from UserMixin
# a database model is just a layout or blueprint for an object that is going to be stored in the database


class User(db.Model, UserMixin):
    # defining the columns to store in this table, all of the users will be stored in this schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


''' when there is one to many relationship i.e one object many children, in this case we have 1 user that has many notes.
we store a foreign key on the child objects that reference the parent object'''


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
