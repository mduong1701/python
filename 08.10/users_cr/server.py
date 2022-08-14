from flask import Flask, request, render_template, session, redirect
from user import User

app = Flask(__name__)
app.secret_key = "It's a secret to everyone"

@app.route("/users")
def index():
    current_users = User.get_all()
    return render_template("index.html", current_users = current_users)

@app.route("/users/new")
def new():
    return render_template("new.html")

@app.route("/users/add", methods=["POST"])
def add():
    data = {
        "first_name" : request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    new_id = User.save(data)
    new_data = {
        "id": new_id
    }
    single_user = User.get_one(new_data)
    return render_template("single_user.html", single_user = single_user)

@app.route("/users/<int:id>/view")
def single_user_page(id):
    data = {
        "id": id
    }
    single_user = User.get_one(data)
    return render_template("single_user.html", single_user = single_user)

@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")

@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        "id": id
    }
    single_user = User.get_one(data)
    return render_template("edit_user_page.html", single_user = single_user)

@app.route("/users/<int:id>/submit_edit", methods=["POST"])
def submit_edit(id):
    data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.edit_user(data)
    return redirect("/users")





if __name__ == "__main__":
    app.run(debug=True)

