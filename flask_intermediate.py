
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

#When you open SQL workbench use schematics to find the database Lance and typer into script "USE Lance" then type 
# "SELECT *
#FROM Users"
#this will show you all the values in the table Users


#mycursor.execute("CREATE DATABASE Lance")
#mycursor.execute("CREATE TABLE Users(name VARCHAR(20),password VARCHAR(300), userID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("ALTER TABLE Users MODIFY password VARCHAR(255);")
#mycursor.execute("SHOW DATABASES")

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
        create_user_name=request.json["name"]
        create_user_pass=request.json["password"]
        create_user_email=request.json["email"]
        create_hashed_password=pass_hash(create_user_pass)
        mycursor.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (create_user_name, create_hashed_password))
        db.commit()
        

        print("Received POST data:", create_user_name, create_user_pass, create_user_email)
        print("Hashed password:", create_hashed_password)

        print("Redirecting to /user...") 

        return redirect("/user")
    else:
        return render_template("create_account.html") 


@app.route("/Lance/login", methods=["POST","GET"])
def Login():
    if request.method == "POST":
        log_user_name=request.json["name"]
        log_user_pass=request.json["password"]
        mycursor.execute("SELECT * FROM Users WHERE name=%s",(log_user_name,))
        user = mycursor.fetchone()
        if user:
            print("user found:",user)

            store_pass=user[1]

            if pass_hash(log_user_pass) == store_pass:
                print("passwords match", user)
                return redirect("/Lance/Welcome")
            else:
                print("Incorrect Password",)
                return redirect("/Lance/login")
        else:
            print("User not found")
            return redirect("/Lance/login")
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
