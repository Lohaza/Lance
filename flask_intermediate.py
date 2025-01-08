
import hashlib
import mysql.connector
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)



db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Lance"
    
)

mycursor=db.cursor()
#mycursor.execute("CREATE DATABASE Lance")
#mycursor.execute("CREATE TABLE Users(name VARCHAR(20),password VARCHAR(300), userID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("ALTER TABLE Users MODIFY password VARCHAR(255);")

mycursor.execute("SELECT * FROM Users")

for x in mycursor:
    print(x)

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
        mycursor.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (user_name, hashed_password))
        db.commit()
        

        print("Received POST data:", user_name, user_pass, user_email)
        print("Hashed password:", hashed_password)

        print("Redirecting to /user...") 

        return redirect("/user")
    else:
        return render_template("create_account.html") 


@app.route("/Lance/login")
def Login():
    return render_template("Login.html")


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
