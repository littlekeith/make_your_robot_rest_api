# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)


def get_current_day(_format="%Y-%m-%d"):
    """
    get current date, return _format is %Y%m%d%H
    """
    import datetime
    return datetime.datetime.now().strftime(_format)


class UserLogin(Resource):

    def get(self):

        username = g.args.get('username', None)
        password = g.args.get('password', None)
        print(username, password)
        if not username or not password:
            response = jsonify({"msg": "Missing username or password !"})
            response.status_code = 400
            return response

        if username != 'test' or password != 'test':
            response = jsonify({"msg": "Bad username or password"})
            response.status_code = 401
            return response

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        response = jsonify({'login': True, 'access_token': access_token})

        response.status_code = 200

        return response
