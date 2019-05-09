# -*- coding : utf-8 -*-
# @Time      :2019/4/15 1:30
# @Author    : py15期   lemon_huihui
# @File      : my_test_suite.py
# -*- coding : utf-8 -*-
# @Time      :2019/3/22 20:29
# @Author    : py15期   lemon_huihui
# @File      : UT.py
import unittest,sys,HTMLTestRunnerNew
from class_01.test_interface.common import HTMLTestRunnerNew
from class_01.test_interface.testcases.test_recharge import TestRecharge
from class_01.test_interface.common.contants import html_file
class MyTestSuite():
    def __init__(self):
        self.st = unittest.TestSuite()  ##创建套件
        self.ld = unittest.TestLoader()  ###鸟枪换炮了，来个大型加载器
        self.runner = unittest.TextTestRunner()  ##创建执行器

    def addOne_case(self,case):
        self.st.addTest(case)##添加单条用例

    def addMany_case(self,cases):
        self.st.addTests(cases)  ##添加多条

    def addModule_case(self,module):
        self.st.addTest(self.ld.loadTestsFromModule(module))##加载一个模块

    def addClass_case(self,object):
        self.st.addTest(self.ld.loadTestsFromTestCase(object))##加载一个类
        #self.st.addTest(unittest.makeSuite(object))

    def addPath_case(self,path,pattern='test*.py'):
        all_cases = unittest.defaultTestLoader.discover(path,pattern)##加载文件目录路径tern
        for case in all_cases:
            self.st.addTests(case)

    def run(self):
        self.runner.run(self.st)  ##走一个

    def run_html(self,stream=sys.stdout, verbosity=2,title=None,description=None,tester=None):
        runner= HTMLTestRunnerNew.HTMLTestRunner(stream, verbosity,title,description,tester)
        runner.run(self.st)

if __name__ == '__main__':
    s=MyTestSuite()
    path = r'D:\lemon_py\class_01\test_interface\testcases'
    s.addPath_case(path)
    with open(html_file,'wb') as fp:
        s.run_html(stream=fp, title='request模块单元测试',description='用例：get、post、密码为空、密码错误等',tester='灰灰的')