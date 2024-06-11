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


# run application
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
