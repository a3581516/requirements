# -*- coding : utf-8 -*-
# @Time      :2019/4/14 0:56
# @Author    : py15期   lemon_huihui
# @File      : test_recharge.py
import unittest,HTMLTestRunnerNew,json
from ddt import ddt,data,unpack
from class_01.test_interface.common.http_request import HttpRequest1,HttpRequest2
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from class_01.test_interface.common.my_log import MyLog
from class_01.test_interface.common.my_db import MyDB
@ddt
class TestRecharge(unittest.TestCase):
    do_excel = DoExcel(filename=case_file, sheet_name='recharge')  # register login recharge
    cases = do_excel.get_cases()

    logger = MyLog('前程贷接口测试')


    @classmethod
    def setUpClass(cls):
        cls.logger.info('Start Recharge!'.rjust(30))
        cls.mydb = MyDB()
        cls.http_request2 = HttpRequest2()

    @data(*cases)
    def test_recharge(self,case):###充值 用例  1带cookies方式发起请求
        self.logger.info("---------------------------------------------------")
        self.logger.info('现在执行第 {} 条,title:{}'.format(case.case_id, case.title,case.check_sql))
        if case.check_sql is not None:
            sql = eval(case.check_sql)['sql1']
            member = self.mydb.get_one(sql)
            print('before是:',member['leaveamount'])
            before = member['leaveamount']

        self.logger.info('请求的参数是：{}'.format(case.data))
        resp = self.http_request2.request(url=case.url, method=case.method, data=case.data)
            # print(resp.text)
        try:
            self.assertEqual(resp.json()["msg"], json.loads(case.expected)["msg"])  ###json字符串
            res = 'PASS'

            if case.check_sql is not None:
                sql = eval(case.check_sql)['sql1']
                member = self.mydb.get_one(sql)
                print(member)
                after = member['leaveamount']
                print(int(eval(case.data)['amount']),'amount..........')
                recharge_amount = int(eval(case.data)['amount'])  # 充值金额

                self.assertEqual(before+recharge_amount,after)


        except AssertionError as e:
            self.logger.error('断言出错，出错信息是{}'.format(e))
            res='FAIL'
            # return None
            raise e
        finally:
            self.logger.info('*******************开始写入数据*******************')
            self.do_excel.write_result(row=case.case_id + 1, actual=resp.text, result=res)
            self.logger.info('*******************结束写入数据*******************')

    @classmethod
    def tearDownClass(cls):
        # cls.http_request2.close()#这里也可以关闭
        cls.logger.info('The end Recharge!'.rjust(30))
        cls.mydb.close()

if __name__ == '__main__':
    unittest.main()

















