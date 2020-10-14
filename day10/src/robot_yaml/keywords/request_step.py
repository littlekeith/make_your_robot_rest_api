#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


@keyword
def set_cookies(session, cookies):
    logger.info(session, cookies)
    if not cookies:
        return cookies
    testin = BuildIn()
    if not isinstance(cookies, dict):
        raise Exception("cookies must be dict")
    if not variables_exists(cookies):
        session.cookies.update(cookies)
        return cookies
    tmp = cookies.copy()
    for key, value in cookies.items():
        _value = testin.get_variable_value(value)
        tmp[key] = str(_value)
        # tmp['domain'] = hostname
        session.cookies.set(key, str(_value), path='/', domain=hostname)

    # session.cookies.update(tmp)
    logger.info(session.cookies)
    return tmp


@keyword
def set_headers(session, headers):

    if not headers:
        return headers
    testin = BuildIn()
    if not isinstance(headers, dict):
        raise Exception("headers must be dict")
    if not variables_exists(headers):
        session.headers = headers
        return headers
    tmp = headers.copy()
    for key, value in headers.items():
        # todo: value is variable
        _value = testin.bi.get_variable_value(value)
        tmp[key] = _value

    session.headers = tmp
    logger.info(session.headers)
    return tmp


@keyword(name='ts_create_session')
def init_session(url):
    testin = BuildIn()
    testin.set_suite_variable(SESSION_NAME, requests.Session())
    session = testin.run_keyword('create_session', url)
    testin.set_suite_variable(SESSION_NAME, session)
    # print(11111111111)

    return session
