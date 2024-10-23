# -*- coding: utf-8 -*-
import os
from flask import Flask

app = Flask(__name__)


@app.route('/about', methods=['GET'])
def about():
    version = '0.1.0'
    return {
        'version': version
    }, 200

@app.route('/secret', methods=['GET'])
def secret():
    return {
        'DB_PASSWORD': os.environ.get('DB_PASSWORD')
    }, 200
