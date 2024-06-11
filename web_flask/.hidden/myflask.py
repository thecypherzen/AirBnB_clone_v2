#!/usr/bin/python3

from flask import Flask

app  = Flask(__name__)


@app.route('/', strict_slashes=False)
def default_route():
    """do somethings"""
    return "This is default route."


@app.route('/<val>', strict_slashes=False)
def handle_value(val):
    """route handling value"""
    return f"You entered the value {val}"



if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
