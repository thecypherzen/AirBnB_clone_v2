#!/usr/bin/python3
"""A flask app serving hbnb version 2"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes storage session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """fetches sorted list of all states in db"""
    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)
    states = list(map(lambda state: state.to_dict(), states))
    print(states[0])
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
