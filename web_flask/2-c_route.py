#!/usr/bin/python3
"""A simple flask application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """defines the base app route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """defines an hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_route(text):
    """defines a route handling text variable """
    return ("C " + text.replace("_", " "))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
