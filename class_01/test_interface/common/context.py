# -*- coding : utf-8 -*-
# @Time      :2019/4/21 10:27
# @Author    : py15期   lemon_huihui
# @File      : context.py
import re,configparser
from class_01.test_interface.common.read_config import config
from class_01.test_interface.common.my_log import MyLog


logger = MyLog('读取配置文件')

##在正则替换上面 定个 类，来存放 动态参数
class Context:
    loan_id = None
    loan_member_id =None





def replace(data):
    '''
    方案:利用search找到第一个就返回的特点， 我们使用找到一个就替换一个的策略
    第一个已经换完 ，继续循环找,的下一个，以此类推，找到就返回 group(1) 换，没找到返回None
    '''
    pattern = '#(.*?)#'
    while re.search(pattern,data):# 返回 None  就是 Flase，不会继续循环了

        res = re.search(pattern,data)###打印分组 group(1) ，  0 或 不传 返回所有

        g1 = res.group(1)# 获取到参数化的key

        #首先去找配置文件 ，没有再找类属性
        try:
            value = config.get_str('data',g1)#根据#key 配置文件里取
        except configparser.NoOptionError as e:
            logger.error('配置文件{}没有{}'.format('data',g1))

            # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context,g1):  #查看类 是否存在 属性g1   ，有就取
                value = getattr(Context,g1)
            else:                                                 #没有就打印 消息
                logger.error('contants类 属性 也找不到参数化的值')
                raise e

        logger.info('参数化的值{}：{}'.format(g1,value))

        # 按 模式 匹配 sub查找并替换 会找到两个 所有要指定count= 1
        new_data = re.sub(pattern,repl=value,string=data,count=1)

        # 循环 继续判断 data
        data = new_data

    return data
