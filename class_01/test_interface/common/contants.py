# -*- coding : utf-8 -*-
# @Time      :2019/4/13 16:29
# @Author    : py15期   lemon_huihui
# @File      : contants.py
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #
# print(base_dir)
# print(os.path.split(os.path.dirname(__file__))[0])
case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
log_file = os.path.join(base_dir, 'log','test_http_request.log')
html_file = os.path.join(base_dir, 'reports','test_http_request.html')

global_file = os.path.join(base_dir, 'config','global.cfg')

online_file = os.path.join(base_dir, 'config','online.cfg')
sit_file = os.path.join(base_dir, 'config','sit.cfg')
uat_file = os.path.join(base_dir, 'config','uat.cfg')
# print(case_file)
