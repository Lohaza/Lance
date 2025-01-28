
import hashlib
import logging
import mysql.connector
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename


app= Flask(__name__, static_folder='static')
CORS(app)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
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

#CREATE DATABASE Lance;
#USE Lance


# This to create Users
#CREATE TABLE IF NOT EXISTS Users (
#    userID INT PRIMARY KEY AUTO_INCREMENT,
#    name VARCHAR(20) NOT NULL,
#    password VARCHAR(255) NOT NULL,
#    profile_image VARCHAR(255), 
#    email VARCHAR(255)
#);

# This to create guide
#CREATE TABLE IF NOT EXISTS guide (
#    guideID INT PRIMARY KEY AUTO_INCREMENT,
#    guidename VARCHAR(20) NOT NULL, 
#    auther VARCHAR(255)
#);

#mycursor.execute("INSERT INTO guide (guidename) VALUES (%s)",(["harrisguide"]))
mycursor.execute("SELECT * FROM Users")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM guide")

for x in mycursor:
    print(x)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def pass_hash(user_pass):
    hash_pass = hashlib.sha256(user_pass.encode())
    hashed_pass=(hash_pass.hexdigest())
    return hashed_pass

@app.route('/Lance/upload_profile_image', methods=['POST'])
def upload_profile_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(file_path)
        file.save(file_path)

        # Get user_id from session and update database
        user_id = session.get('user_id')

        if user_id:
            mycursor.execute("UPDATE Users SET profile_image = %s WHERE userID = %s", (filename, user_id))
            db.commit()
            return jsonify({"message": "Profile image uploaded successfully", "image_path": filename,}), 200
        
        return jsonify({"error": "User not logged in"}), 401
    else:
        return jsonify({"error": "Invalid file type. Only PNG, JPG, JPEG, and GIF are allowed."}), 400

@app.route("/Lance/Create_your_account", methods=["POST","GET"])
def create_your_account():
    if request.method == "POST":
        create_user_name=request.json["name"]
        create_user_pass=request.json["password"]
        create_user_email=request.json["email"]
        create_hashed_password=pass_hash(create_user_pass)
        mycursor.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (create_user_name, create_hashed_password))
        db.commit() 
        return redirect("/Lance/login",)
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

                store_pass=user[2]

                if pass_hash(log_user_pass) == store_pass:
                    print("passwords match", user)
                    session['user_id'] = user[0]
                    session['username'] = user[1]
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



@app.route("/Lance/image_upload")
def image_upload():
    if "user_id" in session:
        username=session.get("username")
        return render_template("image_upload.html", username=username)
    else:
        return render_template("image_upload.html",username= None)

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
            mycursor.execute("SELECT profile_image FROM Users WHERE userID = %s", (session['user_id'],))
            user = mycursor.fetchone()
            if user and user[0]:
                image_path = user[0]

            else:
                image_path = "default_profile.png"
            
            return render_template("Profile.html", username=username, image_path=image_path)
    
    return render_template("Profile.html", username=None)


@app.route("/Lance/search", methods=["POST","GET"])
def search():
    if "user_id" in session:
        username = session.get("username")
        if request.method == "POST":
            create_search=request.json["search"]
            print("Received POST data:",create_search)
            
            return render_template("search.html",username=username)
        else:
            return render_template("search.html",username=username)
    else:
        if request.method == "POST":
            create_search=request.json["search"]
            print("Received POST data:")
            return render_template("search.html",username=None)
        else:
            return render_template("search.html",username=None)



@app.route('/favicon.ico')
def favicon():
    return '', 204

def index():
    session['username'] = [0]
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
