#coding=gbk
# --------------------------------------------------
# !/usr/bin/python
# PN: pytestDemo
# FN: test_demo
# Author: xiaxu
# DATA: 2022/8/17
# Description:
# ---------------------------------------------------
import pytest,os,time
import allure

def test_01():
    print("test01")
    assert 2==2


def test_012():
    print("test02")
    assert 2==2


def test_03():
    print("test03")
    assert 2==2

def test_05():
    print("test05")
    assert 2==2

@pytest.mark.skip(reason = "no need this test")
def test_06():
    print("test06")
    assert 2 == 2

def test_07():
    print("testbye-bye")
    assert 2 == 2

@pytest.mark.skip(reason = "no need")
def test_08():
    raise Exception("oops")

@allure.issue("172.16.32.113/zentao") #在报告中以链接的形式出现
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert True

@allure.feature("这是关于alure测试写的demo1")
@allure.story("百度测试")
#@pytest.mark.usefixtures("browser")
class TestBaidu:
    @allure.title("百度搜索功能测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_baidu_case01(self,browser):
        """
        1.输入网址
        2.输入搜索信息
        3.点击搜索
        4 断言结果
        :return:
        """
        driver = browser
        with allure.step("step1:输入网址"):
            driver.get("http://www.baidu.com")
        time.sleep(1)
        with allure.step("step2:搜索内容"):
            driver.find_element_by_id('kw').send_keys('狗狗币')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(1)
        allure.attach("my attach","hello,world")
        assert driver.title == "11狗狗币_百度搜索"

    def test_02(self,browser):
        driver = browser
        driver.get("https://www.163.com")
        assert True

if __name__ == '__main__':
    pytest.main(["-s","-v","--alluredir=./tmp/my_allrue_results",'--clean-alluredir'])
    #os.system("allure generate -c ./tmp/my_allrue_results")
    os.system("allure generate --clean ./tmp/my_allrue_results --output ./reporter/")
