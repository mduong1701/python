from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = "It's a secret to everybody"

@app.route("/")
def index():
    if "random_num" not in session:
        session["random_num"] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)