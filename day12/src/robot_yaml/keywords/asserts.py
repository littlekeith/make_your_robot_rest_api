#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Convenience functions for testing both in unit and higher levels.

Benefits:
  - Integrates 100% with unittest (see example below)
  - Can be easily used without unittest (using unittest.TestCase when you
    only need convenient asserts is not so nice)
  - Saved typing and shorter lines because no need to have 'self.' before
    asserts. These are static functions after all so that is OK.
  - All 'equals' methods (by default) report given values even if optional
    message given. This behavior can be controlled with the optional values
    argument.

Drawbacks:
  - unittest is not able to filter as much non-interesting traceback away
    as with its own methods because AssertionErrors occur outside.

Most of the functions are copied more or less directly from unittest.TestCase
which comes with the following license. Further information about unittest in
general can be found from http://pyunit.sourceforge.net/. This module can be
used freely in same terms as unittest.

unittest license::

    Copyright (c) 1999-2003 Steve Purcell
    This module is free software, and you may redistribute it and/or modify
    it under the same terms as Python itself, so long as this copyright message
    and disclaimer are retained in their original form.

    IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
    SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
    THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
    DAMAGE.

    THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
    AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
    SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

Examples::

    import unittest
    from robot.utils.asserts import assert_equal

    class MyTests(unittest.TestCase):

        def test_old_style(self):
            self.assertEqual(1, 2, 'my msg')

        def test_new_style(self):
            assert_equal(1, 2, 'my msg')

Example output::

    FF
    ======================================================================
    FAIL: test_old_style (example.MyTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "example.py", line 7, in test_old_style
        self.assertEqual(1, 2, 'my msg')
    AssertionError: my msg

    ======================================================================
    FAIL: test_new_style (example.MyTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "example.py", line 10, in test_new_style
        assert_equal(1, 2, 'my msg')
      File "/path/to/robot/utils/asserts.py", line 181, in assert_equal
        _report_inequality_failure(first, second, msg, values, '!=')
      File "/path/to/robot/utils/asserts.py", line 229, in _report_inequality_failure
        raise AssertionError(msg)
    AssertionError: my msg: 1 != 2

    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    FAILED (failures=2)
"""

from robot.utils.robottypes import type_name
from robot.utils.unic import unic
from robot.api.deco import keyword
from robot.api import logger
from robot.utils.asserts import assert_not_none, assert_equal
from robot_yaml.parsing.dpath_json import get_value_by_path
from robot_yaml.config.settings import DEBUG

def _debug_response(response, dpath, first=None, second=None):
    if DEBUG:
        logger.info("Response was: {}".format(response))
        if dpath:
            logger.info("Dpath was: {}".format(dpath))
        if first:
            logger.info("The real value was: {}".format(first))
        if second:
            logger.info("The expected value was: {}".format(second))

@keyword
def assert_status_code(response, expect_status_code):
    status_code = response.status_code
    if DEBUG:
        logger.info("Response was: {}".format(response))
        logger.info("Response status code was: {}".format(status_code))
        logger.info("Expected status code was: {}".format(expect_status_code))
    assert_equal(status_code, expect_status_code)


@keyword
def should_be_not_none(src):
    _debug_response(src)
    assert_not_none(src)


def fail(msg=None):
    """Fail test immediately with the given message."""
    _report_failure(msg)


@keyword
def assert_false_by_dpath(response, dpath, msg=None):
    """Fail the test if the expression is True."""
    expr = get_value_by_path(response, dpath)
    _debug_response(response, dpath, expr)
    if expr:
        _report_failure(msg)


@keyword
def assert_true_by_dpath(response, dpath, msg=None):
    """Fail the test unless the expression is True."""
    expr = get_value_by_path(response, dpath)
    _debug_response(response, dpath, expr)
    if not expr:
        _report_failure(msg)


@keyword
def assert_not_none_by_dpath(response, dpath, msg=None, values=True):
    """Fail the test if given object is None."""
    _msg = 'is None'
    obj = get_value_by_path(response, dpath)
    _debug_response(response, dpath, obj)
    if obj is None:
        if msg is None:
            msg = _msg
        elif values is True:
            msg = '%s: %s' % (msg, _msg)
        _report_failure(msg)


@keyword
def assert_none_by_dpath(response, dpath, msg=None, values=True):
    """Fail the test if given object is not None."""
    obj = get_value_by_path(response, dpath)
    _debug_response(response, dpath, obj)
    _msg = '%r is not None' % obj
    if obj is not None:
        if msg is None:
            msg = _msg
        elif values is True:
            msg = '%s: %s' % (msg, _msg)
        _report_failure(msg)


@keyword
def assert_equal_by_dpath(response, dpath, second, msg=None, values=True, formatter=None):
    """Fail if given objects are unequal as determined by the '==' operator."""
    first = get_value_by_path(response, dpath)
    _debug_response(response, dpath, first, second)
    if not first == second:
        _report_inequality(first, second, '!=', msg, values, formatter)


@keyword
def assert_not_equal_by_dpath(response, dpath, second, msg=None, values=True, formatter=None):
    """Fail if given objects are equal as determined by the '==' operator."""
    first = get_value_by_path(response, dpath)
    _debug_response(response, dpath, first, second)
    if first == second:
        _report_inequality(first, second, '==', msg, values, formatter)


@keyword
def assert_almost_equal_by_dpath(response, dpath, second, places=7, msg=None, values=True):
    """Fail if the two objects are unequal after rounded to given places.

    inequality is determined by object's difference rounded to the
    given number of decimal places (default 7) and comparing to zero.
    Note that decimal places (from zero) are usually not the same as
    significant digits (measured from the most significant digit).
    """
    first = get_value_by_path(response, dpath)
    _debug_response(response, dpath, first, second)
    if round(second - first, places) != 0:
        extra = 'within %r places' % places
        _report_inequality(first, second, '!=', msg, values, extra=extra)


@keyword
def assert_not_almost_equal_by_dpath(response, dpath, second, places=7, msg=None, values=True):
    """Fail if the two objects are unequal after rounded to given places.

    Equality is determined by object's difference rounded to to the
    given number of decimal places (default 7) and comparing to zero.
    Note that decimal places (from zero) are usually not the same as
    significant digits (measured from the most significant digit).
    """
    first = get_value_by_path(response, dpath)
    _debug_response(response, dpath, first, second)
    if round(second - first, places) == 0:
        extra = 'within %r places' % places
        _report_inequality(first, second, '==', msg, values, extra=extra)


def _report_failure(msg):
    if msg is None:
        raise AssertionError()
    raise AssertionError(msg)


def _report_inequality(obj1, obj2, delim, msg=None, values=False,
                       formatter=None, extra=None):
    if not msg:
        msg = _format_message(obj1, obj2, delim, formatter)
    elif values:
        msg = '%s: %s' % (msg, _format_message(obj1, obj2, delim, formatter))
    if values and extra:
        msg += ' ' + extra
    raise AssertionError(msg)


def _format_message(obj1, obj2, delim, formatter=None):
    formatter = formatter or unic
    str1 = formatter(obj1)
    str2 = formatter(obj2)
    if delim == '!=' and str1 == str2:
        return '%s (%s) != %s (%s)' % (str1, type_name(obj1),
                                       str2, type_name(obj2))
    return '%s %s %s' % (str1, delim, str2)
