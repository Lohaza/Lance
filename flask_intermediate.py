
from flask import Flask,render_template, request, url_for, redirect
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)

pass_id=""
con_pass_id=""

@app.route("/Lance/Create_your_account", methods=["POST","GET"])
def create_your_account():
    if request.method == "POST":
        user_name=(request.json["name"])
        user_pass=(request.json["password"])
        user_email=(request.json["email"])
        return [user_name,user_pass,user_email]
    else:
        return render_template("create_account.html") 


@app.route("/Lance/Welcome")
def welcome():
    return render_template("Welcome.html")



@app.route("/user")
def user():
    return f"<h1>Welcome</h1>"


if __name__ == "__main__":
    app.run(debug=True)
