#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 获取testcases中的测试步骤

def check_testcases_node(testcases):
    if not testcases:
        raise Exception(
            "Please check yaml contents, testcases node cannot be empty")


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
