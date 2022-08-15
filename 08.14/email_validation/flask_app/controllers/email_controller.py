from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.email import Email

@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/save_email", methods=["POST"])
def save_email():
    data = {
        "email": request.form["email"]
    }
    temp = request.form["email"]
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    Email.save_email(data)
    all_emails = Email.get_all()
    return render_template("success.html", all_emails = all_emails, temp=temp)
#     new_data = {
#         "id" : new_id
#     }
#     result = Dojo.get_one(new_data)
#     return render_template("result.html", result = result)