#!/usr/bin/env python
# -*- coding: utf-8 -*-
from robot.api import TestSuite
from robot_yaml.utils.commons import get_all_py_files


def create_suite(name):

    return TestSuite(name)


def import_library(suite, library):
    '''
        Import library or self-keyword
    '''

    suite.resource.imports.library('{}'.format(library))


def import_librarys(suite, libs_path):
    '''
        Import self keywords which keywods were python files
    '''
    if not libs_path:
        return

    for path in libs_path:

        libs = get_all_py_files(path)
        for kw_file in libs:
            suite.resource.imports.library('{}'.format(kw_file))
