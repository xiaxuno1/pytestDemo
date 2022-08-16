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
import smtplib


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

@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()