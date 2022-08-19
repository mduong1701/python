# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
# from flask_app.models.dojo import Dojo
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            is_valid = False
            flash("First name must be at least 2 characters!!!", "register")

        if len(data["last_name"]) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters!!!", "register")

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!", "register")

        if len(data["password"]) < 8:
            is_valid = False
            flash("Password must be at least 8 characters!!!", "register")
        if (data["password"]) != (data["confirm"]):
            is_valid = False
            flash("The password does not match!!!", "register")
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        if len(data["email"]) == 0 or len(data["password"]) == 0:
            is_valid = False
        return is_valid

    @classmethod
    def is_exist(cls, data):
        query = "SELECT email FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipe_schema').query_db(query, data)
        if len(results) != 0:
            return True
        else:
            return False
        # emails = []
        # for result in results:

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('recipe_schema').query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipe_schema').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipe_schema').query_db(query,data)
        single_user = cls(result[0])
        return single_user





#     @classmethod
#     def get_all(cls, data):
#         query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"

#         results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
#         ninjas = []

#         for ninja in results:
#             single_ninja = cls(ninja)
#             dojo_data = {
#                 "id": ninja["dojos.id"],
#                 "name": ninja["name"],
#                 "created_at": ninja["dojos.created_at"],
#                 "updated_at": ninja["dojos.updated_at"]
#             }
#             single_ninja.dojo = Dojo(dojo_data)
#             ninjas.append(single_ninja) return ninjas
