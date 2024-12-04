
from flask import Flask,render_template, request, url_for, redirect
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)

pass_id=""
con_pass_id=""

@app.route("/Lance/Create_your_account", methods=["POST","GET"])
def create_your_account():
    if request.method == "POST":
        user_pass = request.form["up"]
        print(user_pass)
        return redirect(url_for("user", usr=user_pass))
    else:
        return render_template("create_account.html")


@app.route("/Lance/Welcome")
def welcome():
    return render_template("Welcome.html")



@app.route("/user")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
