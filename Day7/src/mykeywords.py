#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-23 19:51:05


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


@keyword
def setup_multiple_keywords(msg):
    bi = BuiltIn()
    bi.run_keyword('simple_set_variable', msg)
    bi.run_keyword('simple_show_variable')


@keyword
def simple_set_variable(msg):
    bi = BuiltIn()
    args = ['${testvar}', msg]
    bi.run_keyword('set_suite_variable', *args)


@keyword
def simple_show_variable():
    bi = BuiltIn()
    bi.run_keyword('LOG', '${testvar}')


@keyword
def simple_teardown():
    logger.info("run suite teardown")


@keyword
def simple_function():
    logger.info("simple function")
    return "simple test"


@keyword
def simple_function_with_param(data, index=2, flag=False):
    logger.info("{}:{}:{}".format(data, index, flag))
    return data, index, flag


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
        if len(results) != len(save_var_names):
            raise Exception("return number were different with receive number")

        for index, item in enumerate(results):
            args = [save_var_names[index], item]
            bi.run_keyword(save_var_type, *args)
    # logger.info('{}:{}'.format(kw_args, kw_name))
    # bi.log_variables()
    bi.run_keyword(kw_name, *kw_args)
