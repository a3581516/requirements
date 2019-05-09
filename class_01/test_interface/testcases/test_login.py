# -*- coding : utf-8 -*-
# @Time      :2019/4/14 0:56
# @Author    : py15期   lemon_huihui
# @File      : test_login.py
import unittest,HTMLTestRunnerNew,json
from ddt import ddt,data,unpack
from class_01.test_interface.common.http_request import HttpRequest1,HttpRequest2
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from class_01.test_interface.common.my_log import MyLog


@ddt
class TestLogin(unittest.TestCase):
    do_excel = DoExcel(filename=case_file, sheet_name='login')  # register login recharge
    cases = do_excel.get_cases()  # 对象

    logger = MyLog('前程贷接口测试')

    @classmethod
    def setUpClass(cls):
        cls.logger.info('Start Login!'.rjust(30))
        cls.http_request1 = HttpRequest1()

    @data(*cases)
    def test_login(self,case):
        self.logger.info("---------------------------------------------------")
        self.logger.info('现在执行的是第 {} 条用例'.format(case.case_id))
        self.logger.info('请求的参数是：{}'.format(case.data))
        resp = self.http_request1.request(url=case.url, method=case.method, data=case.data)

        try:
            self.assertEqual(resp.text,case.expected)

            res='PASS'
        except AssertionError as e:
            self.logger.error('断言出错，出错信息是{}'.format(e))
            res='FAIL'

            raise e
        finally:
            self.logger.info('*******************开始写入数据*******************')
            self.do_excel.write_result(row=case.case_id + 1, actual=resp.text, result=res)
            self.logger.info('*******************结束写入数据*******************')

    @classmethod
    def tearDownClass(cls):

        cls.logger.info('The end Login!'.rjust(30))

if __name__ == '__main__':
    unittest.main()















