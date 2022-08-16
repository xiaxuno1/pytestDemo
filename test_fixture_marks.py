# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: test_fixture_marks
# Author: xiaxu
# DATA: 2022/8/16
# Description:
# ---------------------------------------------------
import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass

if __name__ == '__main__':
    pytest.main(["test_fixture_marks.py"])
