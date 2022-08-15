# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.dojo import Dojo
from flask import flash

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"

        new_id = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        
        return new_id

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        ninjas = []

        for ninja in results:
            single_ninja = cls(ninja)
            dojo_data = {
                "id": ninja["dojos.id"],
                "name": ninja["name"],
                "created_at": ninja["dojos.created_at"],
                "updated_at": ninja["dojos.updated_at"]
            }
            single_ninja.dojo = Dojo(dojo_data)
            ninjas.append(single_ninja)
        return ninjas