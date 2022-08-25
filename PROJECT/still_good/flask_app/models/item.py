# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.user import User
from flask import flash


class Item:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.price = data["price"]
        self.quantity = data["quantity"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.address = data["address"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def validate_item(data):
        is_valid = True
        if len(data["name"]) < 5:
            is_valid = False
            flash("Name must be at least 5 characters!!!", "item")

        if float(data["price"]) < 0:
            is_valid = False
            flash("Price must be a positive number!!!", "item")

        if int(data["quantity"]) < 0:
            is_valid = False
            flash("Quantity must be a positive number!!!", "item")

        if len(data["description"]) < 10:
            is_valid = False
            flash("Description must be at least 10 characters!!!", "item")

        if len(data["instruction"]) < 10:
            is_valid = False
            flash("Instruction must be at least 10 characters!!!", "item")
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO items(name, price, quantity, description, instruction, address, created_at, updated_at, user_id) VALUES(%(name)s, %(price)s, %(quantity)s, %(description)s, %(instruction)s, %(address)s, NOW(), NOW(), %(user_id)s);"
        new_id = connectToMySQL('python_project').query_db(query, data)
        return new_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items JOIN users ON items.user_id = users.id;"
        results = connectToMySQL('python_project').query_db(query)
        items = []
        for item in results:
            single_item = cls(item)
            user_data = {
                "id": item["users.id"],
                "first_name": item["first_name"],
                "last_name": item["last_name"],
                "email": item["email"],
                "password": item["password"],
                "created_at": item["created_at"],
                "updated_at": item["updated_at"]
            }
            single_item.user = User(user_data)
            items.append(single_item)
        return items

    @classmethod
    def get_all_by_one_user(cls, data):
        query = "SELECT * FROM items JOIN users ON items.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL('python_project').query_db(query, data)
        items = []
        for item in results:
            single_item = cls(item)
            user_data = {
                "id": item["users.id"],
                "first_name": item["first_name"],
                "last_name": item["last_name"],
                "email": item["email"],
                "password": item["password"],
                "created_at": item["created_at"],
                "updated_at": item["updated_at"]
            }
            single_item.user = User(user_data)
            items.append(single_item)
        return items






    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        result = connectToMySQL('python_project').query_db(query, data)
        item = cls(result[0])
        return item

    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM items WHERE id = %(id)s"
        connectToMySQL('python_project').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE items SET name=%(name)s, price=%(price)s, quantity=%(quantity)s, description=%(description)s, instruction=%(instruction)s, address=%(address)s, updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL('python_project').query_db(query, data)
