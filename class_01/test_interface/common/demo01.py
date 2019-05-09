# -*- coding : utf-8 -*-
# @Time      :2019/4/29 0:26
# @Author    : py15期   lemon_huihui
# @File      : demo01.py
import unittest
from ddt import ddt,data,unpack
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import


@ddt
class TestSendMCode(unittest.TestCase):


    case={"url":"http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl","data":'{"client_ip":"192.168.1.1","tmpl_id":"1","mobile":"13850600551"}'}
    @data(*case)
    def test_sendMCode(self,url,data):
        client = Client(url)

        res = client.service.sendMCode(data).retCode
        print(res)

if __name__ == '__main__':
    unittest.main()








    #
    # t={"channel_id":2,"ip":"129.45.6.7","mobile":"mobile" ,"pwd":"123456",
    #    "user_id" :"shabicu8","verify_code":"123456"}
    # result=client.service.userRegister(t)
    # # client这个对象 ，调用service这个方法，然后再调用userRegister这个接口函数，函数里面传递刚刚我们准备
    # # 好的得参数字典 t
    # print(result)#打印返回结果
    #http://www.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl

    client = Client('http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl')
    print(client.service.getMobileCodeInfo('13850600551', ''))

    imp = Import('http://www.w3.org/2001/XMLSchema',
    location='http://www.w3.org/2001/XMLSchema.xsd')
    imp.filter.add('http://WebXml.com.cn/')
    doctor = ImportDoctor(imp)
    client = Client('http://www.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl', doctor=doctor)
    # print client
    print (client.service.getWeatherbyCityName('上海'))