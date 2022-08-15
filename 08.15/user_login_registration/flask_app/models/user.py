# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
# from flask_app.models.dojo import Dojo
from flask import flash
import re
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
        # self.dojo = None

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data["first_name"]) <= 2:
            is_valid = False
            flash("First name must be at least 2 characters!!!")

        if len(data["last_name"]) <= 2:
            is_valid = False
            flash("Last name must be at least 2 characters!!!")

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!")

        if len(data["password"]) <= 2:
            is_valid = False
            flash("Password must be at least 8 characters!!!")

        if (data["password"]) != (data["confirm"]):
            is_valid = False
            flash("The password does not match!!!")

        return is_valid
#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"

#         new_id = connectToMySQL('dojos_ninjas_schema').query_db(query, data)

#         return new_id

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
#             ninjas.append(single_ninja)
#         return ninjas
