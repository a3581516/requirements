# -*- coding: utf-8 -*-
# @Time      :2019/1/10 0010 下午 11:15
# @Author    : lemon_huihui
# @Email     : 13850600551@163.com
# @QQ        : 360090343
# @File      : class_06.py

###########1   大小写转换  upper()  lower()
str_1='hello'
str_2='PyThoN'
res=str_1.upper()
print('转换后的结果是{}'.format(res))
print('转换后的结果是{}'.format(str_2.lower()))
################2  字符串查找 函数find()
#####单个字符 ，  如果能够找到，就 返回单个字符的 索引值
res=str_1.find('o')
print(res)
#####多个字符 ，  如果能够找到，就 返回多个字符的 第一个元素的 索引值
res=str_1.find('lo')
print(res)
#如果不能够找到，就 返回  -1
res=str_1.find('xx')
print(res)
#########3   字符串的 替换  replace()
str_1=str_1.replace('l','大')###替换 所有指定的元素
print(str_1)

str_1='lllllove'
str_1=str_1.replace('l','大',1)###替换 指定替换次数
print(str_1)

####4字符串的 切割  split()
res=str_1.split('o')######类型还是 字符串 值不过 切完装在 list里
print(res)
####5  字符串  头尾 处理  strip
a='hello lemo '
res=a.strip('o')
print(res)

def call(res=1):
    top3 = ['138', '135', '150']
    while True:
        res = input('请输入您的号码：')
        if res.isdigit():
            for i in res:
                print(res)
                j = res[:3:]
                print(j)
                if j in top3:
                    return print('正在为你拨号请稍后', res)
                else:
                    print('您输入的号码有误，请重新输入')
                    break
        else:
            print('请输入数字字符')
        continue

call()