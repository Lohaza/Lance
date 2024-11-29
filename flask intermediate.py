#pip3 install virtualenv
#pip3 install flask
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("NEA Lance Create your account test.html")

if __name__ == "__main__":
    app.run(debug=True)