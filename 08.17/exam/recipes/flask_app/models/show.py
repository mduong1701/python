# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash


class Show:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.description = data["description"]
        self.release_date = data["release_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None
# =============================================================
    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data["title"]) < 3:
            is_valid = False
            flash("Name must be at least 3 characters!!!", "show")

        if len(data["description"]) < 3:
            is_valid = False
            flash("Description must be at least 3 characters!!!", "show")

        if data["release_date"] == "":
            is_valid = False
            flash("Date must not be blank", "show")

        if len(data["network"]) < 3:
            is_valid = False
            flash("Instruction must be at least 3 characters!!!", "show")
        return is_valid
# =============================================================
    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows(title, network, release_date, description, created_at, updated_at, user_id) VALUES(%(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW(), %(user_id)s);"
        new_id = connectToMySQL('shows_schema').query_db(query, data)
        return new_id
# =============================================================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id;"
        results = connectToMySQL('shows_schema').query_db(query)
        shows = []
        for show in results:
            single_show = cls(show)
            user_data = {
                "id": show["users.id"],
                "first_name": show["first_name"],
                "last_name": show["last_name"],
                "email": show["email"],
                "password": show["password"],
                "created_at": show["created_at"],
                "updated_at": show["updated_at"]
            }
            single_show.user = User(user_data)
            shows.append(single_show)
        return shows
# =============================================================
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows WHERE shows.id = %(id)s;"
        result = connectToMySQL('shows_schema').query_db(query, data)
        show = cls(result[0])
        return show
# =============================================================
    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s"
        connectToMySQL('shows_schema').query_db(query, data)
# =============================================================
    @classmethod
    def edit(cls, data):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s, updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL('shows_schema').query_db(query, data)
# =============================================================
