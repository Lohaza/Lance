#pip install flask
from flask_cors import CORS
from flask import Flask,render_template
app= Flask(__name__)
CORS(app)

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")



if __name__ == "__main__":
    app.run(debug=True)