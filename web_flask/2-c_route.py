#!/usr/bin/python3
""" Starts the hbnb web flask application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """defines default app route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """handles the hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """displays value in 'text' variable """
    output = text.replace('_', ' ')
    return "C " + output


# run application
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
