#!/usr/bin/python3
"""A flask app serving hbnb version 2"""

from flask import Flask, render_template, url_for
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
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

        # get cities in current state
        state_dict["cities"] = []
        for city in state_obj.cities:
            city_dict = city.to_dict()
            city_dict["places"] = [place.to_dict() for place in city.places]

            # get places in current city
            for place in city_dict["places"]:
                place["owner"] = storage.get(User, place["user_id"]).to_dict()
            state_dict["cities"].append(city_dict)
        states_cities.append(state_dict)
    return render_template("100-hbnb.html", amenities=amenities,
                           states=states_cities)


@app.teardown_appcontext
def close_storage(err):
    """Closes storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
