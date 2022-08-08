# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: test_demo01
# Author: xiaxu
# DATA: 2022/8/4
# Description:对demo的测试
# ---------------------------------------------------
import demo01
import pytest

def test_01():
   a= 3
   b = 5
   assert demo01.add(a,b) == a+b

def test_02():
   a = 5
   b = 3
   assert demo01.sub(a,b) == a+b

