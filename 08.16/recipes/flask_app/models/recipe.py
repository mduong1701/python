# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.user import User
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None
# Now we use class methods to query our database
    # @staticmethod
    # def validate_sundae(data):
    #     is_valid = True
    #     if len(data["name"]) < 6:
    #         is_valid = False
    #         flash("Name must have at least 5 characters!")

    #     if len(data["sauce"]) < 6:
    #         is_valid = False
    #         flash("Sauce must have at least 5 characters!")

    #     if int(data["num_scoops"]) == 0:
    #         is_valid = False
    #         flash("Number of scoops must be more than 0!")

    #     if len(data["flavor"]) < 6:
    #         is_valid = False
    #         flash("Flavor must have at least 5 characters!")
        
    #     return is_valid

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM sundaes JOIN shops ON sundaes.shops_id = shops.id;"
    #     # # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('sundaes_schema').query_db(query)
    #     # # Create an empty list to append our instances of friends
    #     sundaes = []
    #     # # Iterate over the db results and create instances of Sundae with cls.
    #     ## A list of dictionaries become a list of objects
    #     for sundae in results:
    #         single_sundae = cls(sundae)
    #         shop_data = {
    #             "id": sundae["shops.id"],
    #             "name": sundae["shops.name"],
    #             "created_at": sundae["shops.created_at"],
    #             "updated_at": sundae["shops.updated_at"]
    #         }
    #         single_sundae.shop = Shop(shop_data)
    #         sundaes.append(single_sundae)
    #     return sundaes

    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO sundaes(name, flavor, num_scoops, topping1, topping2, container, sauce, shops_id, created_at, updated_at) VALUES(%(name)s, %(flavor)s, %(num_scoops)s, %(topping1)s, %(topping2)s, %(container)s, %(sauce)s, %(shops_id)s, NOW(), NOW());"
    #     new_id = connectToMySQL('sundaes_schema').query_db(query, data)
    #     return new_id

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM sundaes JOIN shops ON sundaes.shops_id = shops.id WHERE sundaes.id = %(id)s;"
    #     results = connectToMySQL('sundaes_schema').query_db(query, data)
    #     if (len(results)) < 1:
    #         return False

    #     single_sundae = cls(results[0])
    #     shop_data = {
    #         "id": results[0]["shops.id"],
    #         "name": results[0]["shops.name"],
    #         "created_at": results[0]["shops.created_at"],
    #         "updated_at": results[0]["shops.updated_at"]
    #     }
    #     single_sundae.shop = Shop(shop_data)
    #     return single_sundae

    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM sundaes WHERE id = %(id)s"
    #     connectToMySQL('sundaes_schema').query_db(query, data)

    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE sundaes SET name=%(name)s, flavor=%(flavor)s, num_scoops=%(num_scoops)s, topping1=%(topping1)s, topping2=%(topping2)s, sauce=%(sauce)s, shops_id=%(shops_id)s, updated_at=now() WHERE id=%(id)s;"

    #     connectToMySQL('sundaes_schema').query_db(query, data)
