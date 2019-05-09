# -*- coding : utf-8 -*-
# @Time      :2019/4/21 2:04
# @Author    : py15期   lemon_huihui
# @File      : test_invest.py

import unittest,HTMLTestRunnerNew,json
from ddt import ddt,data,unpack
from class_01.test_interface.common.context import Context
from class_01.test_interface.common import context
from class_01.test_interface.common.http_request import HttpRequest1,HttpRequest2
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from class_01.test_interface.common.my_log import MyLog
from class_01.test_interface.common.my_db import MyDB

@ddt
class TestInvest(unittest.TestCase):
    do_excel = DoExcel(filename=case_file, sheet_name='invest')  # register login recharge
    cases = do_excel.get_cases()

    logger = MyLog('前程贷接口测试')

    @classmethod
    def setUpClass(cls):
        cls.logger.info('Start Invest!'.rjust(30))
        cls.http_request2 = HttpRequest2()
        cls.mysql = MyDB()
    @data(*cases)
    def test_invest(self, case):  ###2带session方式发起请求
        self.logger.info("---------------------------------------------------")
        self.logger.info('现在执行第 {} 条,title:{}'.format(case.case_id, case.title))
        # 1） case.data = eval(case.data)
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #      case.data['mobilephone'] = config.get_str('data','normal_user')

        # 2）设计用例变量 提高参数灵活性。用正则遍历所有替换
        case.data = context.replace(case.data)

        self.logger.info('请求的参数是：{}'.format(case.data))

        resp = self.http_request2.request(url=case.url, method=case.method, data=case.data)
        print(resp.text)
        try:
            self.assertEqual(resp.json()["code"], json.loads(case.expected)["code"])  ###json字符串
            res = 'PASS'
            if resp.json()['msg'] == '加标成功':#我们就去查数据库的最新标的 id 存在类里


                sql =  "select id from future.loan where memberid = 1201 order by id desc limit 1"
                loan_id = self.mysql.get_one(sql)['id']
                print('数据库loan_ID是',loan_id)
                print('前面',getattr(Context, "loan_id"))
                setattr(Context,"loan_id",str(loan_id))#数据库查询出来的是int
                print('后面',getattr(Context,"loan_id"))




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
        cls.http_request2.close()  # 这里也可以关闭
        cls.logger.info('The end Invest!'.rjust(30))
        cls.mysql.close()


if __name__ == '__main__':
    unittest.main()














