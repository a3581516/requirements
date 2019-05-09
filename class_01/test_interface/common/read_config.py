# -*- coding : utf-8 -*-
# @Time      :2019/3/17 15:17
# @Author    : py15期   lemon_huihui
# @File      : read_config.py
from class_01.test_interface.common import contants
from configparser import ConfigParser


class  ReadConfig():
    def __init__(self):
        self.cf = ConfigParser()#实例化一个对象
        self.cf.read(contants.global_file,encoding='utf-8')#打开配置文件
        res =  self.cf.getint('swicth','on')#写死了这里首先就读取 global 的 on

        if res == 1:#选择环境
            self.cf.read(contants.sit_file)
        elif res == 2:
            self.cf.read(contants.uat_file)
        elif res == 3:
            self.cf.read(contants.online_file)
        else:
            print('请输入 1、 2、 3')
####下面是读取 配置项####
    def sections(self):
        return self.cf.sections()#查看所有 标签

    def options(self,sec):
        return self.cf.options(sec)#查看所在标签的所有选项

    def items(self,sec):
        return self.cf.items(sec)#查看所在标签的 键值 list返回

    def dict(self,sec):          #查看所在标签的 键值 dict返回
        d={}
        for i in self.items(sec):#调用上面封装的items
            d[i[0]]=i[1]
        return d

    def get_str(self,section,option):#以str格式获取
        return self.cf.get(section,option)

    def get_int(self,section, option):#以int格式获取
        return self.cf.getint(section, option)

    def get_float(self,section, option):#以float格式获取
        return self.cf.getfloat(section, option)

    def get_boolean(self,section, option):#以bool值格式获取
        return self.cf.getboolean(section, option)


  #############################下面获取值   函数#########################


#为了方便调用 什么事都做得出来
config = ReadConfig()

if __name__ == '__main__':
    pass






