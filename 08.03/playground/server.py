from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/<times>/<color>")
def play(color, times):
    return render_template("index.html", num_times = int(times), box_color = color)

if __name__ == "__main__":
    app.run(debug = True)