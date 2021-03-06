"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

# -*- coding: utf-8 -*-

##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.Text, db.ForeignKey('brands.name'), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    brand = db.relationship('Brand')

    def __repr__(self):
        return "<Model id=%d year=%d brand name=%s name=%s>" % (self.id, 
            self.year, self.brand_name, self.name)

class Brand(db.Model):

    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer, nullable=True)

    models = db.relationship('Model')

    def __repr__(self):
        return "<Model id=%d name=%s founded=%d headquarters=%s>" % (self.id, 
            self.name, self.founded, self.headquarters)
        # for brands in Brand:
        #     if discontinued == NULL:
        #         return "<Brand id=%d brand name=%s year founded=%d headquartered in=%s>" % (self.id, 
        #             self.name, self.founded, self.headquarters)
        #     else:
        #         return "<Brand id=%d brand name=%s year founded=%d headquartered in=%s> discontinued=%d" % (self.id, 
        #             self.name, self.founded, self.headquarters, self.discontinued)

# End Part 1
##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

    db.create_all()
