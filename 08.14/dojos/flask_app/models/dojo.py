# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data["name"]) < 3:
            is_valid = False
            flash("Name must be at least 3 characters!!!")
        
        if data["location"] == "":
            is_valid = False
            flash("A location option must be selected!!!")

        if data["language"] == "":
            is_valid = False
            flash("A language option must be selected!!!")
        
        if len(data["comment"]) < 3:
            is_valid = False
            flash("Comment must be at least 3 characters!!!")

        return is_valid
    @classmethod
    def save_survey(cls, data):
        query = "INSERT INTO dojos(name, location, language, comment, created_at, updated_at) VALUES(%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        new_id = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return new_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
            
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)

        result = cls(results[0])
        return result