from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} for {total} fruits")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    