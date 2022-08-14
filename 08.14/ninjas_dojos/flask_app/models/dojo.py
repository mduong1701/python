# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # # Create an empty list to append our instances of friends
        dojos = []
        # # Iterate over the db results and create instances of Sundae with cls.
        ## A list of dictionaries become a list of objects
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        new_id = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return new_id
