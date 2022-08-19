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


@pytest.mark.skip(reason = "no need currently testing this")
def test_01():
    print("这是test01")

@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.7 or higher")
def test_02():
    print("这是测试02")

@pytest.mark.slow
def test_03():
    print("这是测试03")

@pytest.mark.xfail
def test_04():
    print("这是测试04")
    assert 2==4

@pytest.mark.xfail(raises=RuntimeError)
def test_05():
    print("这是测试05")
    assert 2==4

@pytest.mark.xfail(run=False)
def test_06():
    print("这是测试06")
    assert 2==4

@pytest.mark.xfail(strict=True)
def test_07():
    print("这是测试07")
    assert 2==2

if __name__ == '__main__':
    pytest.main(["-rx","test_mark_demo1.py"])
