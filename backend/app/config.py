import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gametester:password@localhost/game_database' #MAKE SURE TO MAKE A USER AND DATABASE FOR THIS
    SQLALCHEMY_TRACK_MODIFICATIONS = False

