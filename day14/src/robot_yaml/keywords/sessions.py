#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


@keyword
def log_session(session):
    print(dir(session))


@keyword
def update_header_key(key, value, session=None):

    if not session:
        headers = {}
    else:
        headers = session.headers
        logger.info("update session")
    logger.info("old headers: {}".format(headers))
    logger.info("update headers key: {}, value: {}".format(key, value))
    headers[key] = value
    logger.info("newer headers: {}".format(headers))

    if session:
        session.headers = headers

    return headers
