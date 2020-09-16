#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect


__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

sys.path.insert(0, os.path.join(__location__, '../../src'))

# default report, log and output name: test.*
default_report_name = 'test'
# default outputs path: outputs folder
default_path = os.path.join(__location__, '../outputs')
print(os.path.exists(default_path))
if not os.path.exists(default_path):
    os.makedirs(default_path)

options = {
    "output": "{}-output.xml".format(default_report_name),
    "log": "{}-log.html".format(default_report_name),
    "report": "{}-reporter.html".format(default_report_name),
    "outputdir": default_path,
    # "include": ['CI']
    # "exclude": ['SMOKE']
}
