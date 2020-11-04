# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


class UserLogout(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        print(dir(g))
        response = jsonify(msg="Log out")
        response.status_code = 200

        return response
