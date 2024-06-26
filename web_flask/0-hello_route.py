#!/usr/bin/python3
""" Starts the hbnb web flask application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


# run app
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
