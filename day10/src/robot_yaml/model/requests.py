#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot_yaml.model.teststeps import create_keyword


def send_request(test, method, uri, data=None, session=None, assign=[]):
    if not test:
        raise Exception("need a testcase obj")

    if not method:
        raise Exception("request method should be: get, post, head, delete...")

    method = method.lower()
    if method == 'get':
        create_keyword(test, 'get_request', [
                       session, uri], assign=assign)

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
                       session, uri, "data={}".format(data)], assign=assign)

        return 'post_request'
    elif method == 'put':
        create_keyword(test, 'put_request', [
                       session, uri, data], assign=assign)

        return 'put_request'
    elif method == 'patch':
        create_keyword(test, 'patch_request', [
                       session, uri, data], assign=assign)

        return 'patch_request'
    elif method == 'delete':
        create_keyword(test, 'delete_request', [
                       session, uri], assign=assign)

        return 'delete_request'
