#!/usr/bin/python3
""" Create Flask app"""
import getenv from os
import Flask from flask
import storage from models
import app_views from api.v1.views

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST;, '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(hosts=HOST, port=PORT, threaded=True)
