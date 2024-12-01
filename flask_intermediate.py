
from flask import Flask,render_template, request,jsonify
from flask_cors import CORS
app= Flask(__name__, static_folder='static')
CORS(app)

pass_id=""
con_pass_id=""

@app.route("/Lance/Create_your_account")
def create_your_account():
    return render_template("create_account.html")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    pass_id = data.get('password_id')
    con_pass_id = data.get('confirm_password_id')
    print(f"pass Input ID: {pass_id}")
    print(f"con_pass Input ID: {con_pass_id}")

    return jsonify({'message': 'IDs received successfully', 'pass_id': pass_id, 'con_pass_id': con_pass_id})

if __name__ == "__main__":
    app.run(debug=True)