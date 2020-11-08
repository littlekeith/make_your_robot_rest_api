# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Date    : 2020-07-23 16:53:58


# import sys
# import robot
# from robot.api import logger
# from robot.utils.asserts import assert_not_none
# from robot.api import TestSuite
# from robot.api import ResultWriter
# from robot.conf import RobotSettings

# from ruamel.yaml import YAML
# from ruamel.yaml.constructor import SafeConstructor

# def yaml_to_obj(yaml_file):

#     import codecs
#     yaml = YAML()
#     yaml.allow_duplicate_keys = True

#     try:
#         with codecs.open(yaml_file, 'rb', 'utf-8') as f:
#             datas_dict = yaml.load(f)
#             if not datas_dict:
#                 raise Exception("Please check the file: {}".format(yaml_file))
#             return datas_dict

#     except Exception as e:
#         raise e


# def get_yaml_configures(yaml_obj):
#     if not yaml_obj:
#         raise Exception("get_yaml_configures parameter cannot be empty")

#     return yaml_obj.get('config')


# def get_yaml_cases(yaml_obj):
#     if not yaml_obj:
#         raise Exception("get_yaml_cases parameter cannot be empty")

#     return yaml_obj.get('testcases')


# yaml_file = '..\\cases.yaml'
# print(yaml_to_obj(yaml_file))
# yaml_obj = yaml_to_obj(yaml_file)
# configs = get_yaml_configures(yaml_obj)
# testcases = get_yaml_cases(yaml_obj)

# suite_name = configs.get('suite_name')
# librarys = configs.get('librarys')


# suite = TestSuite(suite_name)
# for _lib in librarys:
#     print(_lib)
#     suite.resource.imports.library('{}'.format(_lib))
# for case in testcases:
#     test_case_name = case.get('name')
#     tags = case.get('tags')
#     steps = case.get('steps')
#     assertions = case.get('assertions')

#     test = suite.tests.create(test_case_name, tags=tags)
#     for step in steps:
#         kw_name = step.get('keyword')
#         kw_args = step.get('args')
#         kw_type = step.get('type')
#         test.keywords.create(kw_name, args=kw_args, type=kw_type)
#         # test.keywords.create(kw_name, args=list(kw_args), type=kw_type)
#     for assert_step in assertions:
#         kw_name = assert_step.get('keyword')
#         kw_args = assert_step.get('args')
#         # print(111, kw_args, type(kw_args))
#         test.keywords.create(kw_name, args=kw_args)

# path = "reports"
# apiname = 'skynet'
# options = {
#     "output": "{}-output.xml".format(apiname),
#     "log": "{}-log.html".format(apiname),
#     "report": "{}-reporter.html".format(apiname),
#     "outputdir": path,
#     # "include": ['CI']
#     "exclude": ['SMOKE']
# }
# settings = RobotSettings(options)
# suite.configure(**settings.suite_config)
# result = suite.run(settings, critical='smoke')

# ResultWriter(settings.output if settings.log
#              else result).write_results(
#     report=settings.report, log=settings.log)


import requests
import json
session = requests.Session()
data = {'username': 'test', 'password': 'test'}
headers = {
    "accept": "application/xml",

    "Connection": "keep-alive",
}

resp = session.get('http://127.0.0.1:5000/v2/user/login',
                   params=data)

print(resp.status_code, resp.text)
# print(dir(session))
print(session.cookies)
# access_token = resp.json().get('access_token')
# headers = {
#     "Authorization": "Bearer " + access_token,
#     "access_token_cookie": access_token
# }
resp = session.get('http://127.0.0.1:5000/v2/user/logout')
print(resp.status_code, resp.text)
