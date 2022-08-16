# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: yeild_demo1
# Author: xiaxu
# DATA: 2022/8/8
# Description:
# ---------------------------------------------------
# content of test_emaillib.py
import pytest,sys


import sys
import pytest


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(
            10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected

if __name__ == '__main__':
    pytest.main(["-rx","parametrize_demo1.py"])
