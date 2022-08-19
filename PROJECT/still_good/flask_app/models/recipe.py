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
        self.Instruction = data["Instruction"]
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["name"]) < 10:
            is_valid = False
            flash("Name must be at least 10 characters!!!", "recipe")

        if len(data["description"]) < 10:
            is_valid = False
            flash("Description must be at least 10 characters!!!", "recipe")

        if len(data["Instruction"]) < 10:
            is_valid = False
            flash("Instruction must be at least 10 characters!!!", "recipe")
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes(name, description, Instruction, under, created_at, updated_at, user_id) VALUES(%(name)s, %(description)s, %(Instruction)s, %(under)s, NOW(), NOW(), %(user_id)s);"
        new_id = connectToMySQL('recipe_schema').query_db(query, data)
        print(new_id)
        return new_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL('recipe_schema').query_db(query)
        recipes = []
        for recipe in results:
            single_recipe = cls(recipe)
            user_data = {
                "id": recipe["users.id"],
                "first_name": recipe["first_name"],
                "last_name": recipe["last_name"],
                "email": recipe["email"],
                "password": recipe["password"],
                "created_at": recipe["created_at"],
                "updated_at": recipe["updated_at"]
            }
            single_recipe.user = User(user_data)
            recipes.append(single_recipe)
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipe_schema').query_db(query, data)
        recipe = cls(result[0])
        return recipe

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        connectToMySQL('recipe_schema').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, Instruction=%(Instruction)s, under=%(under)s, updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL('recipe_schema').query_db(query, data)


# def edit(cls, data):
#     query = "UPDATE sundaes SET name=%(name)s, flavor=%(flavor)s, num_scoops=%(num_scoops)s, topping1=%(topping1)s, topping2=%(topping2)s, sauce=%(sauce)s, shops_id=%(shops_id)s, updated_at=now() WHERE id=%(id)s;"
#     connectToMySQL('sundaes_schema').query_db(query, data)

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

