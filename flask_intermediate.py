
import hashlib
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)

def pass_hash(user_pass):
    hash_pass = hashlib.sha256(user_pass.encode())
    hashed_pass=(hash_pass.hexdigest())
    return hashed_pass



@app.route("/Lance/Create_your_account", methods=["POST","GET"])
def create_your_account():
    if request.method == "POST":
        user_name=request.json["name"]
        user_pass=request.json["password"]
        user_email=request.json["email"]
        hashed_password=pass_hash(user_pass)

        print("Received POST data:", user_name, user_pass, user_email)
        print("Hashed password:", hashed_password)

        print("Redirecting to /user...") 

        return redirect("/user")
    else:
        return render_template("create_account.html") 


@app.route("/Lance/Welcome")
def welcome():
    return render_template("Welcome.html")

@app.route("/Lance")
def Lance():
    return render_template("Lance.html")

@app.route("/user")
def user():
    return "<h1>Welcome</h1>"

@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
