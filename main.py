from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "error": "No error",
    "name": "Jessica",
    "age": "22"
}

error = {
    "error": "Invalid access key."
}

@app.route("/")
def index():
    return "Go to /api!"

@app.route("/api")
def api():
    passed_data = request.args.to_dict()
    given_key = passed_data["accesskey"]

    if given_key == "Jessica2003":
        return jsonify(data)
    else:
        return jsonify(error)

if __name__ == '__main__':
    app.run()