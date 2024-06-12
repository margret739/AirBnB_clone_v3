#!/usr/bin/python3
"""Flask app"""

import app_views from api.v1.views

@app_views.route('/status')
def api_status():
    """ """

    response = {'status': "OK")
    return jsonify(response)
