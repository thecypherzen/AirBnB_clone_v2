#!/usr/bin/python3
"""A flask app serving hbnb version 2 filter routes"""

from flask import Flask, render_template, url_for
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def populate_fileters():
    """populates filters with locations and amenities"""

    # fetch amenities
    amenity_objs = storage.all(Amenity).values()
    amenities = [amenity.to_dict()["name"] for amenity in amenity_objs]

    # fetch states and cities
    states_cities = []
    state_objs = storage.all(State).values()
    for state_obj in state_objs:
        state_dict = state_obj.to_dict()
        state_dict["cities"] = [city.to_dict()["name"]
                                for city in state_obj.cities]
        states_cities.append(state_dict)
    return render_template("10-hbnb_filters.html",
                           states=states_cities, amenities=amenities)


@app.teardown_appcontext
def close_storage(err):
    """Closes storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
