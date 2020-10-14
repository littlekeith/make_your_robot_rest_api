import os
import sys
import inspect


__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))
print(__location__)

sys.path.insert(0, os.path.join(__location__, '../src'))

from robot_yaml.parsing.yamlreader import YamlReader
from robot_yaml.model.yamldata import YamlData


yaml_file = os.path.join("examples", "cases.yaml")
_reader = YamlReader()
yaml_contents = _reader.yaml_to_dict(yaml_file)
# print(yaml_contents)
if not yaml_contents:
    raise Exception("Please check the yaml file: {}".format(yaml_file))


def get_config(yaml_contents):
    return yaml_contents.get('config')


def get_suite_name(yaml_config_obj):
    return yaml_config_obj.get('name')


def get_librarys(yaml_config_obj):
    return yaml_config_obj.get('librarys')


def get_librarys_path(yaml_config_obj):
    return yaml_config_obj.get('librarys_path')


def get_suite_setup(yaml_config_obj):
    return yaml_config_obj.get('setup')


def get_suite_teardowns(yaml_config_obj):
    return yaml_config_obj.get('teardown')


def get_testcases(yaml_contents):
    return yaml_contents.get('testcases')


def get_test_name(yaml_case_obj):
    return yaml_case_obj.get('name')


def get_test_tags(yaml_case_obj):
    return yaml_case_obj.get('tags')


def get_test_steps(yaml_case_obj):
    return yaml_case_obj.get('steps')


def get_test_assertions(yaml_case_obj):
    return yaml_case_obj.get('assertions')


_datas = YamlData(yaml_file)

_datas.config = get_config(yaml_contents)
_datas.suite_name = get_suite_name(_datas.config)
_datas.librarys = get_librarys(_datas.config)
_datas.librarys_path = get_librarys_path(_datas.config)
_datas.suite_setup = get_suite_setup(_datas.config)
_datas.suite_teardowns = get_suite_teardowns(_datas.config)
_datas.testcases = get_testcases(yaml_contents)
# _datas.test_name = get_test_name(_datas.testcases)
# _datas.test_tags = get_test_tags(_datas.testcases)
# _datas.test_steps = get_test_steps(_datas.testcases)
# _datas.test_assertions = get_test_assertions(_datas.testcases)


print("config: ", _datas.config)
print("suite_name: ", _datas.suite_name)
print("librarys: ", _datas.librarys)
print("librarys_path: ", _datas.librarys_path)
print("suite_setup: ", _datas.suite_setup)
print("suite_teardowns: ", _datas.suite_teardowns)
print("testcases: ", _datas.testcases)
print("test_name: ", _datas.test_name)
print("test_tags: ", _datas.test_tags)
print("test_steps: ", _datas.test_steps)
print("test_assertions: ", _datas.test_assertions)
