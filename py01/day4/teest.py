# all_chs = '1234567890qwertyuiopasdfghjklzxcvbnm'
#
# result = ''
#
# from random import  choice
# for i in range(8):
#     ch = choice(all_chs)
#     result += ch
#
# print(result)

# p = ''
# from random import choice
# for i in range(8):
#     q = choice(n)
#     p += q
#
# print(p)
# random.choice(n)
# def passwd(k=8):
#     import random
#     n = '123456789qwertyuiopasdfghjklzxcvbnm'
#
#     p = ''
#
#     for i in range(k):
#         o = random.choice(n)
#         p += o
#     return p
#
# if __name__ == '__main__':
#     print(passwd(9))

# import os
# def get_fname():
#     while 1:
#         fname = input("文件名: ")
#         if not os.path.exists(fname):
#             break
#         print("文件已存在，请重试。")
#     return fname
#
# def get_content():
#     content = []
#
#     print("请输入内容，在单独的一行上输入end结束！")
#     while 1:
#         line = input("(end to quit)>")
#         if line == "end":
#             break
#         content.append(line)
#
#     return content
#
# def wfile(fname,content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for  line in content]
#     wfile(fname,content)

# import os
#
# def get_file():
#     while 1:
#         n = input("文件名:")
#         if not os.path.exists(n) :
#             break
#         print("文件已存在，请重试。")
#     return n
#
# def get_content():
#     j = []
#     print("sb")
#     while 1:
#         p = input("sb into end: ")
#         if p == "end":
#             break
#         j.app
#     return j
#
# def wirt(min, nei):
#     with open(min, 'w') as work:
#         work.writelines(nei)
#
# if __name__ == '__main__':
#     name = get_file()
#     file = get_content()
#     file = ['%s\n' % p for p in file]
#     wirt(name,file)

import os
#判断文件是否存在
# def file():
while 1:
    n = input("you want to file: ")
    if os.path.exists(n):
        print("file is have")
    else:
        break
    # return n

# def get_fname():
#     "用于获取一个系统中不存在的文件名"
#     while 1:
#         fname = input("文件名: ")
#         if not os.path.exists(fname):
#             break
#         print("文件已存在，请重试。")
#
#     return fname

#
# if __name__ == '__main__':
#     fname = file()

