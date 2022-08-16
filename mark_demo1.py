# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: pytestDemo
# FN: yeild_demo1
# Author: xiaxu
# DATA: 2022/8/8
# Description:
# ---------------------------------------------------
# content of test_emaillib.py
import pytest

from yeild_demo import Email, MailAdminClient


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    print("执行发送用户的创建，在yeild之前")
    user = mail_admin.create_user()
    yield user
    print("执行删除发送的用户，在yeild后")
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    print("执行接收用户的创建，yield前")
    user = mail_admin.create_user()
    yield user
    print("执行接收用户的删除，yield之后")
    mail_admin.delete_user(user)


def test_email_received(sending_user, receiving_user):
    print("开始测试用例....")
    email = Email(subject="Hey!", body="How's it going?")
    print("调用发送模块")
    sending_user.send_email(email, receiving_user)
    print("调用接收模块，assert断言")
    assert email in receiving_user.inbox
    print("程序执行完毕")


if __name__ == '__main__':
    pytest.main(["-s","yeild_demo1.py"])
