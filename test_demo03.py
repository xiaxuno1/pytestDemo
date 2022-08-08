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

def test_demo03_01():
   a= 5
   b = 5
   assert demo01.mult(a,b) == a*b

@pytest.mark.slow
def test_demo03_02():
   a = 5
   b = 5
   print("正在运行标记为slow的用例")
   assert demo01.sub(a,b) == a+b,"断言失败"

def test_demo03_03(info):
   a= 5
   b = 5
   assert demo01.mult(a,b) == a*b

def test_demo03_04(info1):
   a= 5
   b = info1
   assert demo01.mult(a,b) == a+b

def test_zero_division():
   with pytest.raises(ZeroDivisionError):
      1 / 0


def test_recursion_depth():
   with pytest.raises(RuntimeError) as excinfo:
      def f():
         f()

      f()
   assert "maximum recursion" in str(excinfo.value)

if __name__ == '__main__':
   pytest.main(["-k","test_demo03_04"])