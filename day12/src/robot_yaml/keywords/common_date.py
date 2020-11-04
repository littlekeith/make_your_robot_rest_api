#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


@keyword
def get_current_day(_format="%Y-%m-%d"):
    """
    get current date, return _format is %Y%m%d%H
    """
    import datetime
    return datetime.datetime.now().strftime(_format)
