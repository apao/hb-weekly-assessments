"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Model of cars."""

    __tablename__ = "models"
    
    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Represents model object."""

        return "<Model id=%s name=%s year=%s>" % (self.model_id, self.name, self.year)


class Brand(db.Model):
    """Brand of cars."""

    __tablename__ = "brands"
  
    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        """Represents brand object."""

        return "<Brand id=%s name=%s>" % (self.brand_id, self.name)


# cars=# ALTER TABLE brands RENAME COLUMN id TO brand_id;
# ALTER TABLE
# cars=# ALTER TABLE models RENAME COLUMN id TO model_id;
# ALTER TABLE
# cars=# \d brands
#                                    Table "public.brands"
#     Column    |         Type          |                      Modifiers                      
# --------------+-----------------------+-----------------------------------------------------
#  brand_id     | integer               | not null default nextval('brands_id_seq'::regclass)
#  name         | character varying(50) | not null
#  founded      | integer               | 
#  headquarters | character varying(50) | 
#  discontinued | integer               | 
# Indexes:
#     "brands_pkey" PRIMARY KEY, btree (brand_id)

# cars=# \d models
#                                   Table "public.models"
#    Column   |         Type          |                      Modifiers                      
# ------------+-----------------------+-----------------------------------------------------
#  model_id   | integer               | not null default nextval('models_id_seq'::regclass)
#  year       | integer               | not null
#  brand_name | character varying(50) | 
#  name       | character varying(50) | not null
# Indexes:
#     "models_pkey" PRIMARY KEY, btree (model_id)  

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


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
