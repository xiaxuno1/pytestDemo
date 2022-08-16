# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: passdata_demo
# Author: xiaxu
# DATA: 2022/8/16
# Description:传递数据
# ---------------------------------------------------
import pytest


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]

    # Do something with the data
    return data


@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    print(fixt)
    assert fixt == 42

if __name__ == '__main__':
    pytest.main(["-v","passdata_demo.py"])