#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 获取config or testcases中的测试步骤

def check_testcases_node(testcases):
    if not testcases:
        raise Exception(
            "Please check yaml contents, testcases or config node cannot be empty")

# get config steps


def create_test_keywords(suite, yaml_testcase, method, uri, test_obj=None, index=0):
    '''
    1. create test 
    2. send requests
    3. create test keywords
    4. create test assertions

    '''
    from robot_yaml.model import testcases as tc
    from robot_yaml.model.requests import send_request
    # ptn: parse testcases node
    try:

        name = get_case_name(
            yaml_testcase) or "call other api {}".format(str(index))
        tag = get_case_tag(yaml_testcase)

        session_name = get_case_session(yaml_testcase)
        assign_name = get_case_assign(yaml_testcase) or []
        steps = get_case_step(yaml_testcase)
        assertions = get_case_assertion(yaml_testcase)

        test = test_obj or tc.create_test(suite, name, tag)
        send_request(test, method, uri, yaml_testcase,
                     session_name, assign_name)
        tc.create_test_steps(test, steps)
        tc.create_test_assertions(test, assertions)
        return test
    except Exception as e:
        raise e


def init_testcases(suite, cases, method, uri, path=None, api_yamls_obj=None, test_obj=None):
    '''
        This function will do:
            1. create suite.test
            2. create test keywords which are testcases in reference api yaml node[Option]
            3. create test keywords which are self yaml 
        Example: Logout need Login first, we assume run logout test, then need call login 
                 You will see two Test: Login and Logout
                 If you use second option:
                 You will see one Test: Logout, but keywords include login keywords
        suite -- testsuites object
        case -- yaml testcases node
        method -- request method
        uri -- request uri
        path -- other api yaml files path
        api_yamls_obj -- config apis node
        test_obj -- suite test object
    '''
    # ptn: parse testcases node
    from robot_yaml.model import testcases as tc
    for index, tcase in enumerate(cases):

        # run other api testcases first
        create_test_keywords_of_other_apis(suite, path, api_yamls_obj)
        # run self testcases
        create_test_keywords(
            suite, tcase, method, uri, index=index)

        # second options
        # name = get_case_name(
        #     tcase) or "call other api {}".format(str(index))
        # tag = get_case_tag(tcase)
        # test = test_obj or tc.create_test(suite, name, tag)
        # # run other api testcases first
        # create_test_keywords_of_other_apis(suite, path, api_yamls_obj, test)
        # # run self testcases
        # create_test_keywords(
        #     suite, tcase, method, uri, test, index)


def create_test_keywords_of_other_apis(suite, path, api_yamls_obj, test_obj=None):
    '''
    1. Read yaml contents
    2. create test keywords
    '''

    import os
    from robot_yaml.parsing.yamlreader import YamlReader
    from robot_yaml.running import get_config_and_testcases

    if not api_yamls_obj:
        return

    try:
        reader = YamlReader()

        for index, api_case in enumerate(api_yamls_obj):
            file = api_case.get('file')
            file = os.path.join(path, file)
            _api_contents = reader.yaml_to_dict(file)
            configs, testcases = get_config_and_testcases(_api_contents)

            
            method = get_request_method(configs)
            uri = get_request_uri(configs)
            create_test_keywords(
                suite, testcases, method, uri, test_obj, index)
    except Exception as e:
        raise e


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


def get_case_data(case):
    '''
    get testcases data
    '''

    from robot_yaml.datas.yaml_fields import TEST_DATA

    check_testcases_node(case)

    return case.get(TEST_DATA)


def get_case_params(case):
    '''
    get testcases params
    '''

    from robot_yaml.datas.yaml_fields import TEST_PARAMS

    check_testcases_node(case)

    return case.get(TEST_PARAMS)


def get_case_json(case):
    '''
    get testcases json
    '''

    from robot_yaml.datas.yaml_fields import TEST_JSON

    check_testcases_node(case)

    return case.get(TEST_JSON)


def get_case_session(case):

    from robot_yaml.datas.yaml_fields import TEST_SESSION

    check_testcases_node(case)

    return case.get(TEST_SESSION)

def get_case_assign(case):

    from robot_yaml.datas.yaml_fields import ASSIGN

    check_testcases_node(case)

    return case.get(ASSIGN)
