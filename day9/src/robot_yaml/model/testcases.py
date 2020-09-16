#!/usr/bin/env python
# -*- coding: utf-8 -*-


def create_test(suite, name, tags='smoke'):
    if not suite:
        raise Exception("Need a TestSuite object")

    return suite.tests.create(name, tags=tags)

def create_test_steps(test, steps):

    from robot_yaml.model.teststeps import create_step
    if not steps:
        return

    for index, case in enumerate(steps):
        create_step(test, case)

def create_test_assertions(test, assertion):

    from robot.api import logger
    from robot_yaml.model.teststeps import create_step
    if not assertion:
        logger.warn("If config assertions into yaml file will be better")
        return

    for index, case in enumerate(assertion):
        create_step(test, case)
