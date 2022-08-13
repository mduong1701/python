# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Shop:
    def __init__(self, data):
        self.id = data["id"]
        self.name=data["name"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shops;"
        # # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('sundaes_schema').query_db(query)
        # # Create an empty list to append our instances of friends
        shops = []
        # # Iterate over the db results and create instances of Sundae with cls.
        ## A list of dictionaries become a list of objects
        for shop in results:
            shops.append(cls(shop))
        return shops