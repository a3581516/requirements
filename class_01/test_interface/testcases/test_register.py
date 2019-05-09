# -*- coding : utf-8 -*-
# @Time      :2019/4/14 0:56
# @Author    : py15期   lemon_huihui
# @File      : test_register.py
import unittest,HTMLTestRunnerNew,json
from ddt import ddt,data,unpack
from class_01.test_interface.common.http_request import HttpRequest1,HttpRequest2
from class_01.test_interface.common.doExcel import DoExcel
from class_01.test_interface.common.contants import case_file
from class_01.test_interface.common.my_log import MyLog
from class_01.test_interface.common.my_db import MyDB


@ddt
class TestRegister(unittest.TestCase):
    do_excel = DoExcel(case_file, 'register')  # register login recharge
    cases = do_excel.get_cases()
    logger = MyLog('前程贷接口测试')
    mydb = MyDB()

    @classmethod
    def setUpClass(cls):

        cls.logger.info('Start Register!')
        cls.http_request1 = HttpRequest1()

    @data(*cases)
    def test_register(self,case):
        self.logger.info("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        self.logger.info('现在执行第 {} 条,title:{}'.format(case.case_id,case.title))
        #
        # # 1）data的一个参数进行判断
        # if json.loads(case.data)['mobilephone'] == 'register_mobile':
        #     ##如果找到 就换，先取数据库中最大的手机号码+1  作为 新的注册手机号
        #     new_num = int((MyDB().get_one('select max(mobilephone) from future.member'))[0])+1
        #     ##replace(字符串替换函数实现)   换后是新的字符串   需要重新 赋值给 case.data =
        #     case.data = case.data.replace('register_mobile',str(new_num))


        ## 2） 设计用例变量 提高参数灵活性
        ###如果找到就 返回  索引，没找到就返回 -1 ，不等于 -1 说明就是找到了定义的变量名字 我们就换
        if case.data.find('register_mobile') != -1:
            new_num = (self.mydb.get_one('SELECT * FROM future.member m WHERE m.`mobilephone` = 13850600552')['mobilephone'])
            case.data = case.data.replace('register_mobile', str(int(new_num)+1))

        self.logger.info('请求的参数是：{}'.format(case.data))

        resp = self.http_request1.request(url=case.url, method=case.method, data=case.data)
        # print(resp.text)
        try:
            self.assertEqual(resp.text,case.expected)
            res='PASS'
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

        cls.logger.info('The end Register!')

        cls.mydb.close()

if __name__ == '__main__':
    unittest.main()

















