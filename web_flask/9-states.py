#!/usr/bin/python3
"""A flask app serving hbnb version 2 cities by states"""

from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(err):
    """Closes storage session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """fetches sorted list of all states in db with their cities
    """
    all_states = []
    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)
    for state in states:
        state_dict = state.to_dict()
        state_dict["cities"] = [city.to_dict() for city in state.cities]
        all_states.append(state_dict)
    return render_template("8-cities_by_states.html",
                           states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
