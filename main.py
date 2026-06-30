from flask import Flask, jsonify, request
from json import load
from flask_cors import CORS

data = {
    "arithmetic": {
        "q1": {
            "question": "What is 100/25?",
            "options": ["3", "4", "5", "6", "7"],
            "correctIndex": 1
        },
        
    },
    "algebra": {
        "q1": {
            "question": "Find the value of X: '2x = 16'",
            "options": ["4", "6", "8", "10", "12"],
            "correctIndex": 2
        }
    }
}

PORT = 7777

app = Flask(__name__)
CORS(app)

error = {
    "error": "Invalid access key."
}

@app.route("/")
def index():
    return "<h1>Go to /api!<h1>"

@app.route("/mathsapi")
def api():

    passed_data = request.args.to_dict()
    given_key = passed_data["accesskey"]

    if given_key == "ILoveMath":
        # with open("data.json") as f:
        #     myData = load(f)
        # return jsonify(myData)

        return jsonify(data)
    else:
        return jsonify(error)

if __name__ == '__main__':
    app.run(port=PORT)

