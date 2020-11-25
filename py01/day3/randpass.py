# import random
# # d = []
# all_chiice=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
# # a = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# def suiji():
#     for i in range(1,9):
#        a=random.choice(all_chiice)

# -*- coding:utf-8
import random
import sys
# 随机生成密码
def RandomPasswd( rang=None):
    __numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'W', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']
    if rang == None:
        _Passwd = "".join(random.choice(__numlist) for i in range(8))
    else:
        _Passwd = "".join(random.choice(__numlist) for i in range(int(rang)))
    return _Passwd
# print(RandomPasswd())

RandomPasswd(sys.argv[1])
n = input('you want nubmer: ')

