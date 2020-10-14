#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.utils.asserts import assert_not_none, assert_equal


@keyword
def assert_status_code(response, expect_status_code):
    assert_equal(response.status_code, expect_status_code)


@keyword
def should_be_not_none(src):

    assert_not_none(src)
