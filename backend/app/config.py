import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/databasename' #MAKE SURE TO MAKE A USER AND DATABASE FOR THIS
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from __init__ import create_app, db
app = create_app()

with app.app_context():
    db.create_all()