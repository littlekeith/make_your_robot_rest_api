# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Pet(Resource):

    def post(self):
        print(g.json)

        return None, 405, None

    def put(self):
        print(g.json)

        return None, 400, None