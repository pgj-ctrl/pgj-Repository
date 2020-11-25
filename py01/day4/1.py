#定义从哪些字符中选择
# all_chs = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

#定义用于保存结果的变量
# result = ''
#
# #随机选出字符
# import  sys
# from random import choice
# #随机选出字符，并拼接到到结果
# def passwd(n):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return result
# print(passwd(sys.argv[1]))
# # passwd(sys.argv[1])

import hh

n = int(input('you want to number: '))
print(hh.mk_pwd(n))

