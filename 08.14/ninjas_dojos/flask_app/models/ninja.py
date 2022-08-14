# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.dojo import Dojo
from flask import flash

class Ninja:
    def __init__(self):
        pass