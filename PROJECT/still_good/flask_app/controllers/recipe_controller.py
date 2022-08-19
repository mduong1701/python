from flask_app import app
from flask import Flask, request, render_template, session, redirect
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# @app.route("/recipes/new")
# def add_recipe_page():
#     return render_template("add_recipe_page.html")

# @app.route("/")
# def all_sundaes_page():
#     all_sundaes = Sundae.get_all()
#     return render_template("index.html", all_sundaes = all_sundaes)

# @app.route("/sundaes/create")
# def create_page():
#     all_shops = Shop.get_all()
#     return render_template("create_sundae.html", all_shops=all_shops)

# @app.route("/sundaes/submit", methods=["POST"])
# def submit_sundae():
#     data = {
#         "name": request.form["name"],
#         "flavor": request.form["flavor"],
#         "num_scoops": request.form["num_scoops"],
#         "sauce": request.form["sauce"],
#         "topping1": request.form["topping1"],
#         "topping2": request.form["topping2"],
#         "container": request.form["container"],
#         "shops_id": request.form["shops_id"]
#     }

#     if not Sundae.validate_sundae(data):
#         return redirect("/sundaes/create")

#     Sundae.save(data)
#     return redirect("/")

# @app.route("/sundaes/<int:id>")
# def single_sundae_page(id):
#     data = {
#         "id" : id
#     }
#     single_sundae = Sundae.get_one(data)
#     return render_template("single_sundae.html", single_sundae = single_sundae)

# @app.route("/sundaes/<int:id>/delete")
# def delete_sundae(id):
#     data = {
#         "id": id
#     }

#     Sundae.delete(data)
#     return redirect("/")

# @app.route("/sundaes/<int:id>/edit")
# def edit_page(id):
#     data = {
#         "id" : id
#     }

#     all_shops = Shop.get_all()

#     single_sundae = Sundae.get_one(data)
#     return render_template("edit_sundae.html", single_sundae=single_sundae, all_shops = all_shops)

# @app.route("/sundaes/<int:id>/submit_edit", methods=["POST"])
# def submit_edit(id):
#     data = {
#         "name": request.form["name"],
#         "flavor": request.form["flavor"],
#         "num_scoops": request.form["num_scoops"],
#         "sauce": request.form["sauce"],
#         "topping1": request.form["topping1"],
#         "topping2": request.form["topping2"],
#         "container": request.form["container"],
#         "shops_id": request.form["shops_id"],
#         "id": id
#     }

#     if not Sundae.validate_sundae(data):
#         return redirect(f"/sundaes/{id}/edit")

#     Sundae.edit(data)

#     return redirect("/")

