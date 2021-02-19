from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/landing.html")
def landing():
    return render_template("landing.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/signup.html")
def signup():
    return render_template("signup.html")

if __name__== "__main__":
    app.run(debug=True)
