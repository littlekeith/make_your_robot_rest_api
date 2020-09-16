#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robot.api.deco import keyword
from robot.utils.asserts import assert_not_none


@keyword
def should_be_not_none(src):

    assert_not_none(src)
