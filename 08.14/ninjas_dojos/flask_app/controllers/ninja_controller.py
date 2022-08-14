from flask import Flask, render_template, redirect, session, request
from flask_app import app

@app.route("/dojos")
def main_page():
    return render_template("index.html")