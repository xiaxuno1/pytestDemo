# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: yeild_demo1
# Author: xiaxu
# DATA: 2022/8/8
# Description:
# ---------------------------------------------------
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
if __name__ == '__main__':
    pytest.main(["-rx","parametrize_demo2.py"])
