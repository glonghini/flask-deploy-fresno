from flask import flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return ("oi dona moça leticia")

if __name__ == "__main__":
    app.run(debug=True)
