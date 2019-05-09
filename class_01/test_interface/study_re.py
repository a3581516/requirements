# -*- coding : utf-8 -*-
# @Time      :2019/4/21 2:06
# @Author    : py15期   lemon_huihui
# @File      : study_re.py
import re
from class_01.test_interface.common.read_config import config

add_data = '{"memberId":"15810447878","title":"123456","amount":"1000",' \
        '"loanRate":"234241","loanTerm":"234241"},"loanId":"234241",' \
                 '"loanId":"234241","loanIdloanDateType":"234241",' \
                     '"repaymemtWay":"234241","biddingDays":"234241"}'

data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
###找到一个整体 match = '#normal_user#","pwd":"#normal_pwd#'>
# res= re.search('#.*#',data)# 从任意位置开始找，找到第一个就返回，*后 默认是尽可能多的匹配，简称贪婪匹配
# print(res)
# res= re.search('#.*?#',data) # *? 最多只匹配 0 到 1 次 。search 就是找到第一个就返回
# print(res)

# res= re.findall('#(.*?)#',data)#查找全部 返回放进一个列表里
# print(res)


'''
方案:利用search找到第一个就返回的特点， 我们使用找到一个就替换一个的策略
第一个已经换完 ，继续循环找,的下一个，以此类推，找到就返回 group(1) 换，没找到返回None

'''
pattern = '#(.*?)#'
while re.search(pattern,data):# 返回 None  就是 Flase，不会继续循环了

    res = re.search(pattern,data)###打印分组 group(1) ，  0 或 不传 返回所有
    print(res.group(0))# 返回 所有
    print(res.group(1))#取 第一个组
    g1 = res.group(1)# 获取到参数化的key

    value = config.get_str('data',g1)#根据key 取
    print(value) # 按照匹配出来的变量名，去配置文件里取值
    #按 模式 匹配 sub查找并替换 会找到两个 所有要指定count= 1
    new_ata = re.sub(pattern,repl=value,string=data,count=1)
    data = new_ata
print(data)
