from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(templates="lovely_templates_for_my_project")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
