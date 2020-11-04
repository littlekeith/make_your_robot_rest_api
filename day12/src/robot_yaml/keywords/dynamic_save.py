#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


@keyword
def save_function_result_into_variables(config_functions_infos, kw_name, kw_args):
    ''' 
        1. get function result by dpath and save it into robot variable
        2. saved variable type only support global, suite, test, common variable
        3. run keyword with robot variable
    '''
    from robot_yaml.datas.yaml_fields import NAME, DPATH, KEYWORD, KW_ARGS, KW_TYPE, SAVE_VAR_NAME
    from robot_yaml.parsing.dpath_json import get_value_by_path
    from robot_yaml.utils.commons import run_keyword
    # bi.log(config_functions_infos)

    for func in config_functions_infos:
        name = func.get(KEYWORD)
        args = func.get(KW_ARGS)
        save_var_type = func.get(KW_TYPE)
        save_var_names = func.get(SAVE_VAR_NAME)

        results = run_keyword(name, args)
        logger.info("the receive: {}".format(save_var_names))
        logger.info("the return value: {}".format(results))
        if len(results) < len(save_var_names):
            raise Exception(
                "return number must be bigger or equal with receive number")

        for index, item in enumerate(save_var_names):
            _name = item[NAME]
            _path = item.get(DPATH)
            if not _path:
                # if not dpath, then save function result into variable directory
                args = [_name, results]
            else:
                args = [_name, get_value_by_path(results, _path)]

            if not save_var_type:
                run_keyword('set_test_variable', args)
            else:
                run_keyword(save_var_type, args)

    run_keyword(kw_name, kw_args)


@keyword
def return_func():

    return 'a'


@keyword
def return_func_list():

    return [1, 2, {'a': 1}]


@keyword
def return_func_dict():

    return {'a': 1, 'b': 2}


@keyword
def get_collection():
    return [{'href': 'https://example.com/wp-json/wc/v3/products/22/variations'}]
