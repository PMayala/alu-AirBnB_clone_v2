#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls storage.close()
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all states and their cities
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all states and their cities
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Displays an HTML page with a list of all states and their cities,
    or a specific state and its cities
    """
    states = storage.all(State).values()
    state_obj = None
    if state_id:
        state_key = 'State.' + str(uuid.UUID(state_id))
        state_obj = storage.all(State).get(state_key)
    return render_template('9-states.html', states=states, state=state_obj)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
