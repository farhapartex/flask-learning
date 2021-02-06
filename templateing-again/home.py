from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {}
    context["title"] = "Home Page"
    return render_template("index.html", context=context)

@app.route("/blog")
def blog():
    context = {}
    context["title"] = "Blog Page"
    return render_template("blog.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
