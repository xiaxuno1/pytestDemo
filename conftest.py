# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: conftest
# Author: xiaxu
# DATA: 2022/8/5
# Description:pytest的本地配置文件
# ---------------------------------------------------
import pytest


@pytest.fixture()
def info():
    print("fixture be recalled!")

@pytest.fixture()
def info1():
    return 10

# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


