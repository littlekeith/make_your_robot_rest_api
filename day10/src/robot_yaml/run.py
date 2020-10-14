#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import inspect
import robot
from robot.api import logger


__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

sys.path.insert(0, os.path.join(__location__, '../../src'))


def _get_config_and_testcases(src):

    from robot_yaml.datas.yaml_fields import CONFIG, TESTCASES

    if not src:
        raise Exception("yaml contents was None")

    try:
        return src[CONFIG], src[TESTCASES]
    except KeyError as ke:
        raise Exception("yaml file must have config and testcases node")
    except Exception as e:
        raise e


def robot_run(suite, options):

    from robot.api import ResultWriter
    from robot.conf import RobotSettings
    settings = RobotSettings(options)
    suite.configure(**settings.suite_config)
    result = suite.run(settings, critical='smoke')

    ResultWriter(settings.output if settings.log
                 else result).write_results(
        report=settings.report, log=settings.log)


def init_suite(api_infos):
    '''
        create suite
        import librarys
        suite setup 
        suite teardown
    '''
    from robot_yaml.running import suite as pcn
    # pcn: parse config node
    from robot_yaml.model import teststeps as cs
    suite = pcn.create_suite(api_infos)
    pcn.import_libarary(api_infos, suite)
    pcn.import_libararys(api_infos, suite)
    suite_setup = pcn.get_setup_step(api_infos)
    suite_teardown = pcn.get_teardown_step(api_infos)
    if suite_setup:
        cs.create_step(suite, suite_setup, 'setup')
    if suite_teardown:
        cs.create_step(suite, suite_teardown, 'teardown')

    return suite

def init_testcases(suite, cases, method, uri):

    from robot_yaml.model import testcases as tc
    from robot_yaml.running import case as ptn
    from robot_yaml.model.requests import send_request
    # ptn: parse testcases node
    for index, tcase in enumerate(cases):
        name = ptn.get_case_name(tcase)
        tag = ptn.get_case_tag(tcase)
        payloads = ptn.get_case_payloads(tcase)
        session_name = ptn.get_case_session(tcase)
        assign_name = ptn.get_case_assign(tcase) or []
        steps = ptn.get_case_step(tcase)
        assertions = ptn.get_case_assertion(tcase)

        test = tc.create_test(suite, name, tag)
        send_request(test, method, uri, payloads, session_name, assign_name)
        tc.create_test_steps(test, steps)
        tc.create_test_assertions(test, assertions)


def run(options, api_infos, cases):
    '''
        create suite
        create test
        run test
    '''
    # create suite steps
    from robot_yaml.running import case as ptn
    suite = init_suite(api_infos)
    method = ptn.get_request_method(api_infos)
    uri = ptn.get_request_uri(api_infos)
    init_testcases(suite, cases, method, uri)
    robot_run(suite, options)


def main(yaml_case_file):

    from robot_yaml.parsing.arguments import parse_args
    from robot_yaml.config.settings import options
    args = sys.argv[1:]
    if len(args) == 0:
        # print("Expected at least 1 argument, got 0.")
        print("Try --help for usage information.")
        # sys.exit(252)
        robot_settings_options = options

    else:

        try:
            _args = parse_args(args)
            robot_settings_options = {**options, **_args}

        except Exception as e:
            print(str(e))
            sys.exit(252)

    from robot_yaml.parsing.yamlreader import YamlReader

    try:
        reader = YamlReader()
        yaml_datas = reader.yaml_to_dict(yaml_case_file)

    except Exception as e:
        raise e

    configs, testcases = _get_config_and_testcases(yaml_datas)
    run(robot_settings_options, configs, testcases)


if __name__ == '__main__':
    # file = "test.yaml"
    file = "cases.yaml"
    path = os.path.join("..", "..", file)
    main(path)
