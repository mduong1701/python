from flask import Flask, request, render_template, session, redirect
import random
app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "messages" not in session:
        session["messages"] = []
    return render_template("index.html")

@app.route("/process_money", methods = ["POST"])
def process_money():
    if request.form["building"] == "farm":
        num = random.randint(10, 21)
        session["gold"] += num
        session["messages"].append(f"Earned {num} from the farm")
    elif request.form["building"] == "cave":
        num = random.randint(5, 11)
        session["gold"] += num
        session["messages"].append(f"Earned {num} from the cave")
    elif request.form["building"] == "house":
        num = random.randint(2, 6)
        session["gold"] += num
        session["messages"].append(f"Earned {num} from the house")
    elif request.form["building"] == "casino":
        num = random.randint(-50, 51)
        session["gold"] += num
        if num >= 0:
            session["messages"].append(f"Earned {num} from the casino")
        else:
            session["messages"].append(f"Taken {num} by the casino")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)