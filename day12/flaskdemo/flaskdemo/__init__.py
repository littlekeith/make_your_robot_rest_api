# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v2
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['JWT_SECRET_KEY'] = 'robot_with_yaml'  # Change this!
    # app.json_encoder = JSONEncoder
    jwt = JWTManager(app)
    app.register_blueprint(
        v2.bp,
        url_prefix='/v2')
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
