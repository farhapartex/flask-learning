from flask import Flask, render_template

app = Flask(__name__)
"""
By default, Flask looks in the templates folder in the root level of your app.
Way to add templates:
1. rename template to templates
2. supply a template_folder param to have your template folder recognised by the flask app:
app = Flask(__name__, template_folder='template')
"""
TEMPLATE_NAME = "test.html"

@app.route("/")
def home():
    context = {}
    context["title"] = "Template Page"
    return render_template(TEMPLATE_NAME, context=context)


if __name__ == "__main__":
    app.run(debug=True)
