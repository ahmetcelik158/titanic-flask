from flask import Flask, request, render_template
from waitress import serve
from model import Predictor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        # get input data
        form_dict = request.form.to_dict()
        num_keys = ["Pclass", "Age", "SibSp", "Parch"]
        for key in num_keys:
            form_dict[key] = int(form_dict[key])

        # prediction
        p = Predictor()
        p.load_dict(form_dict)
        _, prob = p.predict()
        return render_template("survival.html", probability=prob)

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)
    