#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_all_py_files(path):
    '''
    find all python files by given path
    '''
    import os
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


def run_keyword(name, args=None):
    '''
        To fix run_keyword() argument after * must be an iterable, not NoneType
    '''

    from robot.libraries.BuiltIn import BuiltIn
    bi = BuiltIn()
    if not args:
        return bi.run_keyword(name)

    return bi.run_keyword(name, *args)
