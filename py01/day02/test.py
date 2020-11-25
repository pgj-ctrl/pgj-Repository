# s1 = 'python'
#
# if 3 > 0:
#     print('yes')
#     print('ok')
#
# if 'tt' in s1:
#     print('string in s1')
# else:
#     print('haha')
#
# if 0.0:
#     print('任何值为0的数字都是假')
#
# if 10:
#     print('非0为真')
#
# if ' ':
#     print('haha')
#
# if (1,2,3):
#     print('xixixi')
#
# if {'name': 'nb'}:
#     print('hahaha')
#     print('name')

# a = 10
# b = 20
# s = a if a < b else b
# print(s)
#
# if a < b:
#     s = a
# else:
#     s = b
# print(s)

# a = int(input('number: '))
#
# if 90 <= a <= 99:
#     print('nb')
# elif 80 <= a < 90:
#     print('haixing')
# elif 70 <= a < 80:
#     print('liang')
# elif 60 <= a < 70:
#     print('jige')
# else:
#     print('laji')



# import random
# # 计算机出的和我出的
# all_choices = ['石头', '剪刀', '布']
# prompt = '''(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2/)'''
# pwin = 0
# cwin = 0
# while 1:
#     if pwin == 2 or cwin == 2:
#         break
#
#     ind = int(input(prompt))
#     player = all_choices[ind]  # 获取用户输入的数字并转成整数
#     computer = random.choice(all_choices)  # 在列表中通过下标取出对应的字符串
#     # 定义玩家赢的情况
#     win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
#     # 输出计算机的选择和我的选择
#     print('你出了 %s , 计算机出了 %s' % (player, computer))
#     # 判断输赢
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player, computer] in win_list:
#         print('\033[33;1mYou WIN ！！！\033[0m')
#         pwin += 1
#     else:
#         print('\033[31;1mYou Lose ！！！\033[0m')
#         cwin += 1