#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-23 16:53:58


import sys
import os
import robot
from robot.api import logger
from robot.utils.asserts import assert_not_none
from robot.api import TestSuite
from robot.api import ResultWriter
from robot.conf import RobotSettings
from robot.libraries.BuiltIn import BuiltIn

from ruamel.yaml import YAML
from ruamel.yaml.constructor import SafeConstructor

def yaml_to_obj(yaml_file):

    import codecs
    yaml = YAML()
    yaml.allow_duplicate_keys = True

    try:
        with codecs.open(yaml_file, 'rb', 'utf-8') as f:
            datas_dict = yaml.load(f)
            if not datas_dict:
                raise Exception("Please check the file: {}".format(yaml_file))
            return datas_dict

    except Exception as e:
        raise e


def get_yaml_configures(yaml_obj):
    if not yaml_obj:
        raise Exception("get_yaml_configures parameter cannot be empty")

    return yaml_obj.get('config')


def get_yaml_cases(yaml_obj):
    if not yaml_obj:
        raise Exception("get_yaml_cases parameter cannot be empty")

    return yaml_obj.get('testcases')


def get_all_py_files(path):
    if not path or not os.path.exists(path):
        raise Exception("Cannot find a path or file: {}".format(path))
    results = []
    for root, dirs, files in os.walk(path):
        if not files:
            raise Exception(
                "Cannot find any keywords files in the path: {}".format(path))
        for file in files:
            if file.endswith('.py'):
                results.append(path + "/" + file)

    return results


def create_test_keyword(suite_test, name, args=None, kw_type=None):

    if not args:
        suite_test.keywords.create(name, type=kw_type)
    else:
        suite_test.keywords.create(name, args=args, type=kw_type)


def create_step(suite_test, obj):

    for step in obj:
        kw_name = step.get('keyword')
        kw_args = step.get('args')
        kw_type = step.get('type')

        create_test_keyword(suite_test, kw_name, kw_args, kw_type)


def create_case_step(suite_test, testcases):
    if not testcases:
        logger.warn("If config test-steps into yaml file will be better")
        return

    create_step(suite_test, testcases)


def create_assertion_step(suite_test, assertions):
    if not assertions:
        logger.warn("If config assertions into yaml file will be better")
        return
    create_step(suite_test, assertions)


def get_setup_or_teardown_numbers(suite_steps, kw_type='setup'):

    numbers = [index for index, item in enumerate(
        suite_steps) if item.get('type') == kw_type]
    if len(numbers) >= 2:
        raise Exception(
            "At least two {} were found in config steps: {}".format(kw_type, suite_steps))


def order_suite_setup_and_teardown(suite_steps):
    '''
    If find teardown and setup in steps,
    then make sure create setup keyword first
    '''
    get_setup_or_teardown_numbers(suite_steps)
    get_setup_or_teardown_numbers(suite_steps, 'teardown')
#
    b_teardown = False
    index_td = 0
    import copy
    cp_steps = copy.deepcopy(suite_steps)
    for index, step in enumerate(suite_steps):

        kw_type = step.get('type')
        if kw_type == 'teardown':
            b_teardown = True
            index_td = index
        if kw_type == 'setup':
            if b_teardown and index > index_td:
                cp_steps[index_td], cp_steps[index] = cp_steps[index], cp_steps[index_td]

    return cp_steps


yaml_file = '..\\cases.yaml'

yaml_obj = yaml_to_obj(yaml_file)
configs = get_yaml_configures(yaml_obj)
testcases = get_yaml_cases(yaml_obj)

suite_name = configs.get('suite_name')
librarys = configs.get('librarys')
librarys_path = configs.get('librarys_path')
suite_steps = configs.get('steps')

suite = TestSuite(suite_name)
for _lib in librarys:
    suite.resource.imports.library('{}'.format(_lib))

# un-comment follows line, see what happen
suite_steps = order_suite_setup_and_teardown(suite_steps)
create_case_step(suite, suite_steps)


for case in testcases:
    test_case_name = case.get('name')
    tags = case.get('tags')
    steps = case.get('steps')
    assertions = case.get('assertions')

    # test = suite.tests.create(test_case_name, tags=tags)
    test = suite.tests.create(test_case_name, tags=tags)
    # test.keywords.create('test_builtin_keyword')
    create_case_step(test, steps)
    create_assertion_step(test, assertions)

path = "reports"
apiname = 'skynet'
options = {
    "output": "{}-output.xml".format(apiname),
    "log": "{}-log.html".format(apiname),
    "report": "{}-reporter.html".format(apiname),
    "outputdir": path,
    # "include": ['CI']
    # "exclude": ['SMOKE']
}
settings = RobotSettings(options)
suite.configure(**settings.suite_config)
result = suite.run(settings, critical='smoke')

ResultWriter(settings.output if settings.log
             else result).write_results(
    report=settings.report, log=settings.log)
