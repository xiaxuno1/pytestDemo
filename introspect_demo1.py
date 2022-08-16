# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: introspect_demo1
# Author: xiaxu
# DATA: 2022/8/16
# Description:Fixtures can introspect the requesting test context
# ---------------------------------------------------
import pytest

smtpserver = "mail.python.org"  # will be read by smtp fixture
def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()

if __name__ == '__main__':
    pytest.main(["-qq","introspect_demo1.py"])