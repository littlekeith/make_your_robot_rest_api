#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# this file to generate suite

def check_config_node(api_infos):
    if not api_infos:
        raise Exception(
            "Please check yaml contents, config node cannot be empty")


def create_suite(api_infos):
    '''

    '''
    from robot_yaml.datas.yaml_fields import NAME
    from robot_yaml.model.testsuites import create_suite
    check_config_node(api_infos)
    try:
        name = api_infos[NAME]
        return create_suite(name)
    except Exception as e:
        raise e


def import_libarary(api_infos, suite):
    '''
        Import library or self-keywords
    '''
    from robot_yaml.datas.yaml_fields import LIBRARYS
    from robot_yaml.model.testsuites import import_library
    from robot.api import logger
    check_config_node(api_infos)

    try:
        _libs = api_infos[LIBRARYS]
        if not _libs:
            logger.warn("library item was none on yaml")
            return

        for _library in _libs:

            import_library(suite, _library)
    except KeyError as ke:
        return
    except Exception as e:
        raise e


def import_libararys(api_infos, suite):
    '''
        Import multiple self-keywords in the path
    '''
    from robot_yaml.datas.yaml_fields import LIBRARYS_PATH
    from robot_yaml.model.testsuites import import_librarys
    from robot.api import logger
    check_config_node(api_infos)

    try:
        _libs = api_infos[LIBRARYS_PATH]
        if not _libs:
            logger.warn("library path item was none on yaml")
            return

        for _lib_path in _libs:
            import_librarys(suite, _lib_path)
    except KeyError as ke:
        return
    except Exception as e:

        raise e


def get_setup_step(api_infos):
    '''
        Get setup of the config node
    '''
    from robot_yaml.datas.yaml_fields import KW_SETUP

    from robot.api import logger
    check_config_node(api_infos)

    try:
        return api_infos.get(KW_SETUP)
    except Exception as e:
        raise e


def get_teardown_step(api_infos):
    '''
        Get setup of the config node
    '''
    from robot_yaml.datas.yaml_fields import KW_TEARDOWN

    from robot.api import logger
    check_config_node(api_infos)

    try:
        return api_infos.get(KW_TEARDOWN)
    except Exception as e:
        raise e
