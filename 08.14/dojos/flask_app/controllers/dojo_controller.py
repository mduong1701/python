from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/save_survey", methods=["POST"])
def save_survey():
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"],
    }

    if not Dojo.validate_survey(data):
        return redirect("/")

    new_id = Dojo.save_survey(data)
    
    new_data = {
        "id" : new_id
    }
    result = Dojo.get_one(new_data)
    return render_template("result.html", result = result)