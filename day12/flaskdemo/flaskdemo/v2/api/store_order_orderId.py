# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class StoreOrderOrderid(Resource):

    def get(self, orderId):

        return {'complete': False}, 200, None

    def delete(self, orderId):

        return None, 400, None