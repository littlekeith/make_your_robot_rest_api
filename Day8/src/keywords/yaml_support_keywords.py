#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Support yaml configure keywords
1. Function config
'''
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


def find_similar_key(expected_key, keys):
    import difflib
    result = []
    for key in keys:

        r = difflib.SequenceMatcher(None, key, expected_key).ratio()
        if r >= 0.5:
            result.append(key)
    return result


def get_all_dpaths(obj):
    '''
    get all response path
    response = {
        "a": {
            "b":1
        },
        "c":2
    }
    return ["a", "a/b", "c"]
    '''
    import dpath.util
    result = []
    for (path, value) in dpath.util.search(obj, ['**'], yielded=True, separator="/"):
        result.append(path)

    return result


def logger_similar_key(response, key):
    keys = get_all_dpaths(response)
    similar_keys = find_similar_key(key, keys)

    if similar_keys:
        print("Similar keys: {}".format(similar_keys))

    else:
        print("Could not find key: {} in the response: {}""".format(key, response))


def foreach(obj, path):

    import dpath.util
    if not obj:
        raise Exception("Need a list or dict parameter")

    if not path:
        raise Exception("Need a path")

    b_found = False
    for (path, value) in dpath.util.search(obj, path, yielded=True, separator="/"):
        # print(path, value)
        b_found = True
        return value

    if not b_found:
        logger_similar_key(obj, path)


@keyword
def simple_show_variable(name):
    logger.info("the value is: {} ".format(name))


@keyword
def simple_function_with_param(data, index=2, flag=False):
    logger.info("{}:{}:{}".format(data, index, flag))
    response = ['123',
                {
                    'test': 'simple test',
                    'name': 'simple name'
                },
                'simple msg'
                ]
    logger.info(response)
    return response


@keyword
def run_function_keyword(step_functions, kw_name, kw_args):
    ''' 
        run functions which also as keywords
        set return value as robot variable
        saved varibale type only support: global, suite, test, common varibale
    '''

    for func in step_functions:
        name = func.get('name')
        args = func.get('args')
        save_var_type = func.get('type')
        save_var_names = func.get('saved_var_names')
        bi = BuiltIn()
        results = bi.run_keyword(name, *args)
        logger.info("the receive: {}".format(save_var_names))
        logger.info("the return value: {}".format(results))
        for index, item in enumerate(save_var_names):
            name = item.get('name')
            _dpath = item.get('dpath')
            # 根据路径获取value
            value = foreach(results, _dpath)
            if value:
                args = [name, value]
                bi.run_keyword(save_var_type, *args)

    bi.log_variables()

    bi.run_keyword(kw_name, *kw_args)
