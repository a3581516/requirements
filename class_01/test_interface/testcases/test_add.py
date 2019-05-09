# -*- coding : utf-8 -*-
# @Time      :2019/4/21 2:03
# @Author    : py15期   lemon_huihui
# @File      : test_add.py

import unittest,HTMLTestRunnerNew,json
from ddt import ddt,data,unpack
from class_01.test_interface.common.http_request import HttpRequest1,HttpRequest2
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from class_01.test_interface.common.read_config import config
from class_01.test_interface.common import context
from class_01.test_interface.common.my_log import MyLog


@ddt
class TestAdd(unittest.TestCase):
    do_excel = DoExcel(filename=case_file, sheet_name='add')  # register login recharge
    cases = do_excel.get_cases()

    logger = MyLog('前程贷接口测试')

    @classmethod
    def setUpClass(cls):
        cls.logger.info('Start Add!'.rjust(30))

        cls.http_request2 = HttpRequest2()

    @data(*cases)
    def test_add(self,case):
        self.logger.info("---------------------------------------------------")
        self.logger.info('现在执行第 {} 条,title:{}'.format(case.case_id, case.title))
        # 1） case.data = eval(case.data)
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get_str('data','normal_user')
        #
        # 2）设计用例变量 提高参数灵活性。用正则遍历所有替换
        case.data = context.replace(case.data)

        self.logger.info('请求的参数是：{}'.format(case.data))

        resp = self.http_request2.request(url=case.url, method=case.method, data=case.data)

        # print(resp.text)
        try:
            self.assertEqual(resp.json()["code"], json.loads(case.expected)["code"])  ###json字符串
            res = 'PASS'
        except AssertionError as e:
            self.logger.error('断言出错，出错信息是{}'.format(e))
            res = 'FAIL'
            # return None
            raise e
        finally:
            self.logger.info('*******************开始写入数据*******************')
            self.do_excel.write_result(row=case.case_id + 1, actual=resp.text, result=res)
            self.logger.info('*******************结束写入数据*******************')

    @classmethod
    def tearDownClass(cls):
        cls.http_request2.close()#这里也可以关闭
        cls.logger.info('The end Add!'.rjust(30))

if __name__ == '__main__':
    unittest.main()

















