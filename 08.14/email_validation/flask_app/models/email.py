# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_email(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
        
    #     if data["location"] == "":
    #         is_valid = False
    #         flash("A location option must be selected!!!")

    #     if data["language"] == "":
    #         is_valid = False
    #         flash("A language option must be selected!!!")
        
    #     if len(data["comment"]) < 3:
    #         is_valid = False
    #         flash("Comment must be at least 3 characters!!!")

    #     return is_valid
    @classmethod
    def save_email(cls, data):
        query = "INSERT INTO emails(email, created_at, updated_at) VALUES(%(email)s, NOW(), NOW());"
        new_id = connectToMySQL('email_schema').query_db(query, data)
        return new_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        emails = []
        results = connectToMySQL('email_schema').query_db(query)

        for result in results:
            emails.append(cls(result))
        
        return emails