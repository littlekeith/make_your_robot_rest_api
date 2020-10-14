#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import robot
from robot.api import logger
from robot.run import USAGE
from robot.utils import ArgumentParser


# type: (Dict[str, Optional[object]]) -> Dict[str, object]
def _delete_none_keys(d):
    keys = set()
    for k in d:
        if d[k] is None:
            keys.add(k)
    for k in keys:
        del d[k]
    return d


def parse_args(args):
    '''
    Use robot parse_args
    Remove none keys
    '''

    options, datasources = ArgumentParser(USAGE,
                                          auto_pythonpath=False,
                                          auto_argumentfile=True,
                                          env_options='ROBOT_OPTIONS'). \
        parse_args(args)

    if len(datasources) > 1 and options['name'] is None:
        options['name'] = 'Suites'

    opts = _delete_none_keys(options)

    return opts
