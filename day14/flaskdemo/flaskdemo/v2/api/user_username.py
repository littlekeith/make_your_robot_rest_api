# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class UserUsername(Resource):

    def get(self, username):

        return {}, 200, None

    def put(self, username):
        print(g.json)

        return None, 400, None

    def delete(self, username):

        return None, 400, None