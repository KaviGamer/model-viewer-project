from classifier import get_prediction
from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route("/add-data", methods=["POST"])

def isnotapplicable():
    Image = request.files.get("abcd")
    prediction = get_prediction(Image)
    return jsonify({
        "pred":prediction
    }),200


if (__name__ == "__main__"):
    app.run(debug=True)