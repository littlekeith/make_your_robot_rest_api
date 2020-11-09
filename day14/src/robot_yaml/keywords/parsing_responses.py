#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot_yaml.parsing.dpath_json import get_value_by_path


@keyword
def extract_variable_from_reponse(response, dpath):
    """
    """
    return get_value_by_path(response, dpath)


@keyword
def save_variable_from_reponse(response, dpath, save_var_name, save_var_type='suite'):
    """
    1. get value from response
    2. set value into variable: set suite variable default
    """
    logger.info(response, dpath, save_var_name)
    _real_value = get_value_by_path(response, dpath)
    bi = BuiltIn()
    if save_var_name == 'test':
        bi.set_test_variable(save_var_name, _real_value)
    elif save_var_type == 'global':
        bi.set_global_variable(save_var_name, _real_value)
    else:

        bi.set_suite_variable(save_var_name, _real_value)
