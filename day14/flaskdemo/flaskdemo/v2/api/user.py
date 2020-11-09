# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


class User(Resource):

    def post(self):
        print(g.json, type(g.json))
        username = g.json.get('username')
        access_token = create_access_token(identity=username)
        response = jsonify(access_token=access_token)
        response.status_code = 200
        return response

        # pass
