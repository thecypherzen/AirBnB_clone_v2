#!/usr/bin/python3
""" Starts the hbnb web flask application """

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """handles python text value"""
    output = text.replace('_', ' ')
    return "Python " + output


@app.route('/number/<int:n>', strict_slashes=False)
def handle_number(n):
    """handles the number route """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render a number template iff n is an int"""
    return render_template("5-number.html", number=n)


# run application
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
