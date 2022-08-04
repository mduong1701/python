from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template("index.html", row = 8, col = 8, color1 = "black", color2 ="red")

@app.route('/4')
def eight_by_four():
    return render_template("index.html", row = 4, col = 8, color1 = "black", color2 ="red")

@app.route('/<int:x>/<int:y>')
def x_by_y(x, y):
    return render_template("index.html", row = y, col = x, color1 = "black", color2 ="red")

if __name__ == "__main__":
    app.run(debug=True)