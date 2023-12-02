from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_world(name):
    return f"Hello, {escape(name)}!"


@app.route("/")
@app.route("/<name>")
def hello_world_name(name=None):
    return render_template('hello.html', name=name)
