# -*- coding : utf-8 -*-
# @Time      :2019/4/15 23:06
# @Author    : py15期   lemon_huihui
# @File      : run_all.py
from class_01.test_interface.common.my_test_suite import MyTestSuite
from class_01.test_interface.common.contants import html_file


suite = MyTestSuite()
path = r'D:\lemon_py\class_01\test_interface\testcases'
suite.addPath_case(path)
with open(html_file, 'wb') as fp:
    suite.run_html(stream=fp, title='前程贷项目接口测试报告',
                   description='用例范围：注册、登录、充值', tester='灰灰的')

