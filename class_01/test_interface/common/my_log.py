# -*- coding : utf-8 -*-
# @Time      :2019/4/15 0:36
# @Author    : py15期   lemon_huihui
# @File      : logger.py
import logging
from class_01.test_interface.common.contants import log_file


class MyLog:
    def __init__(self, log_name):
        self.log_name = log_name
        # 创建收集器 并取名字

    def my_log(self, msg, level):
        logger = logging.getLogger(self.log_name)
        logger.setLevel('DEBUG')  # 收集所有级别
        # 格式为
        formatter = logging.Formatter(
            '%(asctime)s - ''%(levelname)s - ''line:%(lineno)d - ''%(name)s - ''日志信息: %(message)s')

        ch = logging.StreamHandler()  # 设置 渠道  输出到控制台
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)  # 设置格式

        # 输出到 日志文件
        fh = logging.FileHandler(filename=log_file, encoding='utf-8')  # 默认 mode='a'g
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        # 对接
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == 'DEBUG':
            logger.debug(msg)
        if level == 'INFO':
            logger.info(msg)
        if level == 'ERROR':
            logger.error(msg)
        if level == 'WARNING':
            logger.warning(msg)
        if level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(ch)
        logger.removeHandler(fh)

    # 输出一条debug级别的信息
    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    logger = MyLog('前程贷接口测试')
    logger.info('asasasa')
    logger.error('asdasdas')

