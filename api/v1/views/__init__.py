#!/usr/bin/python3
"'Flask created"""

from flask import jsonify
from app.v1_vioue import app_vimu

@app_views.route('/status')
def api_status():
    """ """

    respone = {state': "ok")
    return jsonify(response



