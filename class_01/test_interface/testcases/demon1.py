# -*- coding : utf-8 -*-
# @Time      :2019/4/14 2:40
# @Author    : py15期   lemon_huihui
# @File      : demon1.py
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from ddt import ddt ,data ,unpack
do_excel=DoExcel(filename=case_file,sheet_name='login')
dict_cases=do_excel.get_dict_cases()
print(dict_cases)
import unittest

@ddt
class MyTestCase1(unittest.TestCase):

    @data(*dict_cases)
    @unpack
    def test_normal(self,case_id,title,url,method,expected,data):
        print(case_id,title,url,method,expected,data)

if __name__ == '__main__':
    unittest.main()