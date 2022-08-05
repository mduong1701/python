from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "It's a secret to everybody"

@app.route('/')
def main():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route('/destroy_session', methods=["POST"])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/increase', methods=["POST"])
def increase():
    session["count"] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)