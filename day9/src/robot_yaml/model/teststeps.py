#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run_function(suite_or_test, config_functions, kw_name, kw_args, kw_type):
    ''' 
        run functions which also as keywords
        set return value as robot variable
        saved varibale type only support: global, suite, test, common varibale
    '''
    # print(config_functions)
    name = 'save_function_result_into_variables'
    args = [config_functions, kw_name, kw_args]
    create_keyword(suite_or_test, name, args, kw_type)


def create_keyword(suite_or_test, name, kw_args=None, kw_type=None):
    '''
    '''

    if not kw_args:
        suite_or_test.keywords.create(name, type=kw_type)
    else:
        suite_or_test.keywords.create(name, args=kw_args, type=kw_type)


def create_step(suite_or_test, steps, _type=None):
    '''
        create suite or test step
    '''

    kw_name = steps.get('keyword')
    kw_args = steps.get('args')
    kw_type = _type or steps.get('type')
    config_functions = steps.get('run_func')
    if config_functions:
        run_function(suite_or_test, config_functions,
                     kw_name, kw_args, kw_type)
    else:
        create_keyword(suite_or_test, kw_name, kw_args, kw_type)
