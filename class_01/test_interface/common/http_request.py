# -*- coding : utf-8 -*-
# @Time      :2019/4/13 14:53
# @Author    : py15期   lemon_huihui
# @File      : http_request.py
# -*- coding: utf-8 -*-

import requests, json
from class_01.test_interface.common.read_config import config




class HttpRequest1():
    def request(self, method, url, data=None, json=None, cookies=None):
        method = method.upper()

        url=config.get_str('api','url')+url#拼接url    read_config 已经选好环境切换  自动适配

        if type(data) == str:
            data = eval(data)
        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)

        else:
            return None

        return resp


class HttpRequest2:
    def __init__(self):
        self.session = requests.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()

        url = config.get_str('api', 'url') + url  # 拼接url

        if type(data) == str:
            data=eval(data)

        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)

        else:
            return None
        return resp

    def close(self):
        self.session.close()


if __name__ == '__main__':
    # a=HttpRequest1()
    # url='http://v.juhe.cn/historyWeather/province'
    # #data='=%E6%B7%B1%E5%9C%B3&key=4a94544112eb4c0c229732187b5a47ec'
    # data={'key':'4a94544112eb4c0c229732187b5a47ec'}
    # print(a.request('get',url,data=data).text)
    a=HttpRequest1()
    b = HttpRequest2()
    # 登录
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    resp2 = b.request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    # resp1 = a.request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    print(resp2.text)
    # print('resp1:',resp1.text)
    # 充值
    b.close()
    params = {"mobilephone": "15810447878", "amount": "1000"}
    resp2 = b.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
    # b.close()
    print(resp2.status_code)
    print(resp2.text)
