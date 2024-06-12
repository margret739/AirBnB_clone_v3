#!/usr/bin/python3
"""Flask app"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """ """

    response = {'status': "OK"}
    return jsonify(response)

@app_views.route('/stats')
def get_stats():
    """ """
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'place': storage.count('Place'),
            'reviews': storage.count('Reviews'),
            'states': storage.count('States'),
            'users': storage.count('User')
            }

    return jsonify(stats)
