#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot_yaml.model.teststeps import create_keyword


def set_requests_parameters_into_variable(test, case_obj=None):

    from robot.libraries.BuiltIn import BuiltIn

    keyword_name = 'Set Variable'
    if not case_obj:
        request_data = None
        request_json = None
        request_params = None
        request_headers = None
    else:
        from robot_yaml.running import case as ptn
        request_data = ptn.get_case_data(case_obj) or None
        request_json = ptn.get_case_json(case_obj) or None
        request_params = ptn.get_case_params(case_obj) or None
        request_headers = ptn.get_case_headers(case_obj) or None
    # request_headers = reset_headers_value(request_headers)
    create_keyword(test, keyword_name, [
                   request_data], assign=['${request_data}'])
    create_keyword(test, keyword_name, [
                   request_json], assign=['${request_json}'])
    create_keyword(test, keyword_name, [
                   request_params], assign=['${request_params}'])
    create_keyword(test, keyword_name, [
                   request_headers], assign=['${request_headers}'])


def send_request(test, method, uri, case_obj=None, session=None, assign=[]):
    if not test:
        raise Exception("need a testcase obj")

    if not method:
        raise Exception("request method should be: get, post, head, delete...")

    method = method.lower()
    # create_keyword(test, 'Set Test Variable', ['${get_payloads}', data])
    set_requests_parameters_into_variable(test, case_obj)
    from robot.api import logger

    if method == 'get':

        create_keyword(test, 'get_request', [
                       session, uri, 'headers=${request_headers}', 'params=${request_params}', 'data=${request_data}', 'json=${request_json}'], assign=assign)

        return 'get_request'
    elif method == 'options':
        create_keyword(test, 'options_request', [
                       session, uri], assign=assign)

        return 'options_request'
    elif method == 'head':
        create_keyword(test, 'head_request', [
                       session, uri], assign=assign)

        return 'head_request'
    elif method == 'post':
        create_keyword(test, 'post_request', [
                       session, uri, 'headers=${request_headers}', 'params=${request_params}', 'data=${request_data}', 'json=${request_json}'], assign=assign)

        return 'post_request'
    elif method == 'put':
        create_keyword(test, 'put_request', [
                       session, uri, 'headers=${request_headers}', 'params=${request_params}', 'data=${request_data}', 'json=${request_json}'], assign=assign)

        return 'put_request'
    elif method == 'patch':
        create_keyword(test, 'patch_request', [
                       session, uri, 'headers=${request_headers}', 'params=${request_params}', 'data=${request_data}', 'json=${request_json}'], assign=assign)

        return 'patch_request'
    elif method == 'delete':
        create_keyword(test, 'delete_request', [
                       session, uri, 'headers=${request_headers}', 'params=${request_params}', 'data=${request_data}', 'json=${request_json}'], assign=assign)

        return 'delete_request'
