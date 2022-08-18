from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask import flash
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)

@app.route("/")
def main_page():
    return render_template("index.html")
# ========================================================================
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
    return redirect("/dashboard")
# ========================================================================
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
# ========================================================================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    single_user = User.get_by_id(data)
    all_shows = Show.get_all()
    return render_template("dashboard.html", single_user=single_user, all_shows=all_shows)

# =============================================================

@app.route("/shows/new")
def add_show_page():
    if "user_id" not in session:
        return redirect('/')
    return render_template("add_show_page.html")
# =============================================================
@app.route("/save_show", methods=["POST"])
def save_recipe():
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        "release_date": request.form["release_date"],
        # "release_date": datetime.datetime.strptime(request.form["release_date"], '%Y-%m-%d').strftime('%m/%d/%y'),
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    if not Show.validate_show(data):
        return redirect("/shows/new")
    Show.save(data)
    return redirect("/dashboard")
# =============================================================

@app.route("/view_show/<int:id>")
def view_show(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    info = Show.get_one(data)
    user_data = {
        "id": info.user_id
    }
    user = User.get_by_id(user_data)
    return render_template("view_show.html", info=info, user=user)
# =============================================================
@app.route("/delete/<int:id>")
def delete_show(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    Show.delete_show(data)
    return redirect("/dashboard")
# =============================================================
@app.route("/edit_show/<int:id>")
def edit_show(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    edit_show = Show.get_one(data)
    return render_template("edit_page.html", edit_show = edit_show)
# =============================================================
@app.route("/log_out")
def log_out():
    session.clear()
    return redirect("/")
# =============================================================
@app.route("/save_edit/<int:id>", methods=["POST"])
def save_edit(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id,
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    if not Show.validate_show(data):
        return redirect(f"/edit_show/{id}")
    Show.edit(data)
    return redirect("/dashboard")
# =============================================================