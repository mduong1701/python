from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def main_page():
    # all_dojos = Dojo.get_all()
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    raw_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm": request.form["confirm"],
    }
    
    if not User.validate_register(raw_data):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    if User.is_exist(data):
        flash("This email address has been taken!", "register")
        return redirect("/")
    
    session['user_id'] = User.register(data)

    return render_template("dashboard.html")

@app.route("/login", methods=["POST"])
def login():
    # see if the username provided exists in the database
    data = { 
        "email" : request.form["login_email"] 
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    single_user = User.get_by_id(data)
    all_recipes = Recipe.get_all()
    print(all_recipes)
    return render_template("dashboard.html", single_user=single_user, all_recipes=all_recipes)

@app.route("/recipes/new")
def add_recipe_page():
    return render_template("add_recipe_page.html")

@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "Instruction": request.form["Instruction"],
        # "created_at": request.form["created_at"],
        "under": request.form["under"],
        "user_id": session["user_id"]
    }
    if not Recipe.validate_recipe(data):
        return redirect("/recipes/new")
    Recipe.save(data)
    return redirect("/dashboard")

@app.route("/save_edit/<int:id>", methods=["POST"])
def save_edit(id):
    data = {
        "id": id,
        "name": request.form["name"],
        "description": request.form["description"],
        "Instruction": request.form["Instruction"],
        # "created_at": request.form["created_at"],
        "under": request.form["under"],
        "user_id": session["user_id"]
    }
    if not Recipe.validate_recipe(data):
        return redirect(f"/edit/{id}")
    Recipe.edit(data)
    return redirect("/dashboard")

@app.route("/view_recipe/<int:id>")
def view_recipe(id):
    data = {
        "id": id
    }
    info = Recipe.get_one(data)
    return render_template("view_recipe.html", info=info)

@app.route("/delete/<int:id>")
def delete_recipe(id):
    data = {
        "id": id
    }
    Recipe.delete_recipe(data)
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit_recipe(id):
    data = {
        "id": id
    }
    edit_recipe = Recipe.get_one(data)
    return render_template("edit_page.html", edit_recipe = edit_recipe)

@app.route("/log_out")
def log_out():
    session.clear()
    return redirect("/dashboard")

# class Recipe:
# self.id = data["id"]
#         self.name = data["name"]
#         self.description = data["description"]
#         self.instruction = data["instruction"]
#         self.under = data["under"]
#         self.created_at = data["created_at"]
#         self.updated_at = data["updated_at"]
#         self.user_id = data["user_id"]
#         self.user = None
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
