from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/path")
def home():
    return "<h1>You are in home page</h1>"


@app.route("/path/<place>")
def home_in_place(place):
    return "<h1>You are in " + place + " now"


@app.route("/method", methods=["GET", "POST"])
def http_method():
    return "<h1>Testing http method</h1>"


if __name__ == "__main__":
    app.run(debug=True)
