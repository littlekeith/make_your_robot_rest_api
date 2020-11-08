# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


def get_current_day(_format="%Y-%m-%d"):
    """
    get current date, return _format is %Y%m%d%H
    """
    import datetime
    return datetime.datetime.now().strftime(_format)


class UserLogin(Resource):

    def get(self):
        print(g.args)

        # e_resp = {
        #     "id": 732,
        #     "date_created": "2020-10-26",
        #     "date_modify": get_current_day(),
        #     "weight": -1,
        #     "dimensions": {
        #         "length": "",
        #         "width": "",
        #         "height": ""
        #     },
        #     "attributes": [
        #         {
        #             "id": 6,
        #             "name": "Color",
        #             "option": "Black"
        #         }
        #     ],
        #     "_links": {
        #         "self": [
        #             {
        #                 "href": "https://example.com/wp-json/wc/v3/products/22/variations/732"
        #             }
        #         ],
        #         "collection": [
        #             {
        #                 "href": "https://example.com/wp-json/wc/v3/products/22/variations"
        #             }
        #         ],
        #         "up": [
        #             {
        #                 "href": "https://example.com/wp-json/wc/v3/products/22"
        #             }
        #         ]
        #     }
        # }
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username or not password:
            return jsonify({"msg": "Missing username or password !"}), 400
        

        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
        # response = jsonify(e_resp)
        # response.status_code = 200

        # return response

        # return None, 200, {}
