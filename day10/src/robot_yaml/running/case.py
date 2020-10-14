#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 获取config or testcases中的测试步骤

def check_testcases_node(testcases):
    if not testcases:
        raise Exception(
            "Please check yaml contents, testcases or config node cannot be empty")

# get config steps

def get_request_method(configs):
    from robot_yaml.datas.yaml_fields import METHOD

    check_testcases_node(configs)
    return configs.get(METHOD)

def get_request_uri(configs):
    from robot_yaml.datas.yaml_fields import URI

    check_testcases_node(configs)
    return configs.get(URI)



# get testcases steps

def get_case_name(case):
    from robot_yaml.datas.yaml_fields import NAME

    check_testcases_node(case)

    try:
        name = case[NAME]
        if not name:
            msg = "case name was none on yaml"
            logger.error(msg)
            raise Exception(msg)

        return name
    except KeyError as ke:
        return
    except Exception as e:
        raise e

def get_case_tag(case):

    from robot_yaml.datas.yaml_fields import TEST_TAGS

    check_testcases_node(case)

    return case.get(TEST_TAGS)

def get_case_assertion(case):

    from robot_yaml.datas.yaml_fields import TEST_ASSERTIONS

    check_testcases_node(case)

    return case.get(TEST_ASSERTIONS)

def get_case_step(case):

    from robot_yaml.datas.yaml_fields import TEST_STEPS

    check_testcases_node(case)

    return case.get(TEST_STEPS)


def get_case_payloads(case):
    '''
    get testcases payloads
    '''

    from robot_yaml.datas.yaml_fields import TEST_PAYLOADS

    check_testcases_node(case)

    return case.get(TEST_PAYLOADS)

def get_case_session(case):

    from robot_yaml.datas.yaml_fields import TEST_SESSION

    check_testcases_node(case)

    return case.get(TEST_SESSION)

def get_case_assign(case):

    from robot_yaml.datas.yaml_fields import ASSIGN

    check_testcases_node(case)

    return case.get(ASSIGN)
