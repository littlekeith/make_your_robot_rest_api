#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import inspect
import robot
from robot.api import logger


__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

# sys.path.insert(0, os.path.join(__location__, '../../src'))
sys.path.insert(0, os.path.join(__location__, '..', '..', 'src'))


def robot_run(suite, options):

    from robot.api import ResultWriter
    from robot.conf import RobotSettings
    settings = RobotSettings(options)
    suite.configure(**settings.suite_config)
    result = suite.run(settings, critical='smoke')

    ResultWriter(settings.output if settings.log
                 else result).write_results(
        report=settings.report, log=settings.log)


def run(options, api_infos, cases):
    '''
        create suite
        create test
        run test
    '''

    from robot_yaml.running import case as ptn
    from robot_yaml.running import suite as pcn
    from robot_yaml.config import settings
    # create suite steps
    suite = pcn.init_suite(api_infos)
    # get refrence apis configs
    other_apis = pcn.get_refrence_apis(api_infos)
    method = ptn.get_request_method(api_infos)
    uri = ptn.get_request_uri(api_infos)
    # create test steps
    ptn.init_testcases(suite, cases, method, uri,
                       settings.API_YAML_PATH, other_apis)

    robot_run(suite, options)


def main(yaml_case_file):

    from robot_yaml.parsing.arguments import parse_args
    from robot_yaml.config.settings import options
    from robot_yaml.parsing.yamlreader import YamlReader
    from robot_yaml.running import get_config_and_testcases

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

    try:
        reader = YamlReader()
        yaml_datas = reader.yaml_to_dict(yaml_case_file)
        configs, testcases = get_config_and_testcases(yaml_datas)
        run(robot_settings_options, configs, testcases)

    except Exception as e:
        raise e


if __name__ == '__main__':
    # file = "test.yaml"
    file = "cases.yaml"
    path = os.path.join("..", "..", file)
    main(path)
