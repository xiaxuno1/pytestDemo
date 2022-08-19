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

@allure.issue("172.16.32.113/zentao") #�ڱ����������ӵ���ʽ����
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert True

@allure.feature("���ǹ���alure����д��demo1")
@allure.story("�ٶȲ���")
#@pytest.mark.usefixtures("browser")
class TestBaidu:
    @allure.title("�ٶ��������ܲ���")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_baidu_case01(self,browser):
        """
        1.������ַ
        2.����������Ϣ
        3.�������
        4 ���Խ��
        :return:
        """
        driver = browser
        with allure.step("step1:������ַ"):
            driver.get("http://www.baidu.com")
        time.sleep(1)
        with allure.step("step2:��������"):
            driver.find_element_by_id('kw').send_keys('������')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(1)
        allure.attach("my attach","hello,world")
        assert driver.title == "11������_�ٶ�����"

    def test_02(self,browser):
        driver = browser
        driver.get("https://www.163.com")
        assert True

if __name__ == '__main__':
    pytest.main(["-s","-v","--alluredir=./tmp/my_allrue_results",'--clean-alluredir'])
    #os.system("allure generate -c ./tmp/my_allrue_results")
    os.system("allure generate --clean ./tmp/my_allrue_results --output ./reporter/")
