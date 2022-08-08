# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: test_demo01
# Author: xiaxu
# DATA: 2022/8/4
# Description:对demo的测试
# ---------------------------------------------------
import pytest


#您可以将匹配关键字参数传递给上下文管理器，
# 以测试正则表达式是否匹配异常的字符串表示（类似于 unittest 中的 TestCase.assertRaisesRegex 方法）：
#就是说如果正则表达式匹配成功关键字参数("Exception 123 raised")，则认为是期待的，测试通过
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

