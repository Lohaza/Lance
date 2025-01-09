
import hashlib
import logging
import mysql.connector
from flask import Flask, render_template, request, redirect, jsonify, session
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)

app.secret_key="EdLMg77c5cZJ"

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
    try:
        if request.method == "POST":
            log_user_name=request.json["name"]
            log_user_pass=request.json["password"]

            if not log_user_name or not log_user_pass:
                return jsonify({"error": "Missing username or password."}), 400
        
            mycursor.execute("SELECT * FROM Users WHERE name=%s",(log_user_name,))
            user = mycursor.fetchone()
            if user:
                print("user found:",user)

                store_pass=user[1]

                if pass_hash(log_user_pass) == store_pass:
                    print("passwords match", user)
                    session['user_id'] = user[2]
                    session['username'] = user[0]
                    return jsonify({"message": "Login successful"}), 200
                else:
                    print("Incorrect Password",)
                    return jsonify({"error": "Incorrect password. Please try again."}), 401
            else:
                print("User not found")
                return jsonify({"error": "User not found. Please check your username."}), 404
    except Exception as e:
        logging.error("An error occurred during login: %s", str(e))
        return jsonify({"error": "Internal Server Error. Please try again later."}), 500
    return render_template("Login.html")


@app.route("/Lance/Welcome")
def welcome():
    return render_template("Welcome.html")

@app.route("/Lance")
def Lance():
    if "user_id" in session:
        username=session.get("username")
        return render_template("Lance.html", username=username)
    else:
        return render_template("Lance.html",username= None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect('/Lance')


@app.route("/Lance/Profile/<username>")
def Profile(username):
    if "user_id" in session: 
        session_username = session.get("username")  
        if session_username == username: 
            return render_template("Profile.html", username=username)
    else:
        return render_template("Profile.html", username=None) 

@app.route('/favicon.ico')
def favicon():
    return '', 204

def index():
    session['username'] = [0]
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
