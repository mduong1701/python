from flask import Flask, session, redirect, request, render_template
app = Flask(__name__)
app.secret_key = "It's a secret to everybody"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    session["first_name"] = request.form["first_name"]
    session["city"] = request.form["city"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True)