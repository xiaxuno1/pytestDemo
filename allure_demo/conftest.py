#coding=gbk
# --------------------------------------------------
# !/usr/bin/python
# PN: pytestDemo
# FN: conftest
# Author: xiaxu
# DATA: 2022/8/18
# Description:�������ʧ�ܵĽ�ͼ��ʹ��hook
# ---------------------------------------------------

import os

import allure
import pytest
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):  #û��ûskipҲû�б����xfail���쳣��Ҫ��ͼ�����Ϊfaile�Ľ�ͼ
            with allure.step("���ʧ�ܽ�ͼ������"):
                allure.attach(driver.get_screenshot_as_png(),
                              "ʧ�ܽ�ͼ",allure.attachment_type.PNG)

@pytest.fixture()
def browser():
    global driver
    print("���������")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
    print("test end!")