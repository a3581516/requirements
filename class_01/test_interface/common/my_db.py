# -*- coding : utf-8 -*-
# @Time      :2019/4/16 0:50
# @Author    : py15期   lemon_huihui
# @File      : my_db.py
import pymysql

from class_01.test_interface.common.read_config import config


class MyDB:

    def __init__(self):
        #下面MyDB数据库配置信息 都在配置文件里取
        host = config.get_str('db', 'host')
        user = config.get_str('db', 'user')
        password = config.get_str('db', 'password')
        port = config.get_int('db', 'port')
        #1 创建连接
        self.mydb = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')

        #2 创建 打开游标窗口（比喻成打开一个查询窗口）
        self.cursor = self.mydb.cursor(pymysql.cursors.DictCursor)###pymysql.cursors.DictCursor

    def get_one(self,sql):
        # 游标窗口 执行一条sql

        self.cursor.execute(sql)
        self.mydb.commit()
        return  self.cursor.fetchone()#获取 一条结果)

    def get_all(self,sql):
        self.cursor.execute(sql)#执行sql
        self.mydb.commit()
        return self.cursor.fetchall()#获取 所有结果

    def close(self):
        #关闭 游标窗口
        self.cursor.close()
        #关闭连接
        self.mydb.close()

if __name__ == '__main__':
    res=MyDB().get_one('select max(mobilephone) from future.member')
    print(res[0])
    res1 = MyDB().get_all('select * from future.member limit 10')
    print(res1)
    print(res1[0],res1[5])