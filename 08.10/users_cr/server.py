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
    User.save(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)