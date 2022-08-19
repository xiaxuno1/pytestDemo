#coding=gbk
# --------------------------------------------------
# !/usr/bin/python
# PN: pytestDemo
# FN: conftest
# Author: xiaxu
# DATA: 2022/8/18
# Description:添加用例失败的截图，使用hook
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
        if (report.skipped and xfail) or (report.failed and not xfail):  #没有没skip也没有被标记xfail的异常都要截图，标记为faile的截图
            with allure.step("添加失败截图。。。"):
                allure.attach(driver.get_screenshot_as_png(),
                              "失败截图",allure.attachment_type.PNG)

@pytest.fixture()
def browser():
    global driver
    print("启动浏览器")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
    print("test end!")