#!/usr/bin/python3
"""A flask app serving hbnb version 2 cities by states"""

from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """fetches sorted list of all states in db"""
    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)
    states = list(map(lambda state: state.to_dict(), states))
    return render_template("7-states_list.html", states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def states_cities(id):
    """fetches a state by its id"""
    state = storage.get(State, id)
    if not state:
        return render_template("404_notfound.html")
    cities = [city.to_dict() for city in state.cities]
    return render_template("9-states.html",
                           name=state.to_dict()["name"], cities=cities)


@app.teardown_appcontext
def close_storage(err):
    """Closes storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
