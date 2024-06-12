#!/usr/bin/python3
""" Flask app blueprint"""

import Blueprint from flask

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import*
