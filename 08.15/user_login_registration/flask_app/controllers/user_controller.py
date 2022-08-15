from flask import Flask, render_template, redirect, session, request
from flask_app import app
# from flask_app.models.dojo import Dojo
from flask_app.models.user import User

@app.route("/")
def main_page():
    # all_dojos = Dojo.get_all()
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm": request.form["confirm"],
    }

    if not User.validate_register(data):
        return redirect("/")
# @app.route("/create_dojo", methods = ["POST"])
# def create_dojo():
#     data = {
#         "name":request.form["name"]
#     }
#     Dojo.save(data)
#     return redirect("/dojos")

# @app.route("/add_ninja")
# def add_ninja_page():
#     all_dojos = Dojo.get_all()
#     return render_template("add_ninja_page.html", all_dojos=all_dojos)

# @app.route("/ninja/submit", methods = ["POST"])
# def ninja_submit():
#     data = {
#         "first_name":request.form["first_name"],
#         "last_name":request.form["last_name"],
#         "age":request.form["age"],
#         "dojo_id":request.form["dojo_id"]
#     }

#     Ninja.save(data)
#     return redirect("/dojos")

# @app.route("/dojos/<int:id>")
# def show_ninjas(id):
#     data = {
#         "id" : id
#     }

#     all_ninjas = Ninja.get_all(data)
#     return render_template("all_ninjas.html", all_ninjas = all_ninjas)
