# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas


def get_current_day(_format="%Y-%m-%d"):
    """
    get current date, return _format is %Y%m%d%H
    """
    import datetime
    return datetime.datetime.now().strftime(_format)


class UserLogin(Resource):

    def get(self):
        print(g.args)

        e_resp = {
            "id": 732,
            "date_created": "2020-10-26",
            "date_modify": get_current_day(),
            "weight": -1,
            "dimensions": {
                "length": "",
                "width": "",
                "height": ""
            },
            "attributes": [
                {
                    "id": 6,
                    "name": "Color",
                    "option": "Black"
                }
            ],
            "_links": {
                "self": [
                    {
                        "href": "https://example.com/wp-json/wc/v3/products/22/variations/732"
                    }
                ],
                "collection": [
                    {
                        "href": "https://example.com/wp-json/wc/v3/products/22/variations"
                    }
                ],
                "up": [
                    {
                        "href": "https://example.com/wp-json/wc/v3/products/22"
                    }
                ]
            }
        }
        response = jsonify(e_resp)
        response.status_code = 200

        return response

        # return None, 200, {}
