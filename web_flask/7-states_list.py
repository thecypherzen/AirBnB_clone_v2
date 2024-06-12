#!/usr/bin/python3
""" Starts AirBnb application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exp):
    """ closes storage instance access """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """list states in storage"""

    res = storage.all(State).values()
    states = sorted(res, key=lambda obj: obj.name)
    return render_template('7-states_list.html',
                           states=states)


# run app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
