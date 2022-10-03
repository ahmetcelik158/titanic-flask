from flask import Flask, request
from waitress import serve
from model import Predictor
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    # get input data
    request_json = request.get_json()
    request_dict = json.loads(request_json)

    # prediction
    p = Predictor()
    p.load_dict(request_dict)
    survival, probability = p.predict()
    response = json.dumps({"survival": survival, "probability": probability})

    return response, 200

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)
    