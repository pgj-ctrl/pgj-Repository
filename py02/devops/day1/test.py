# import subprocess
# import os
#
# def ping(host):
#     k = subprocess.run('ping -c2 %s &> /dev/null' % host,shell=True)
#     if k.returncode == 0:
#         print('%s is up' % host)
#     else:
#         print('%s is  down' % host)
#
# if __name__ == '__main__':
#     ips = ('192.168.1.%s' % i for i in range(1,255))
#     for ip in ips:
#         ret_val = os.fork()
#         if not ret_val :
#             ping(ip)
#             exit()

# import threading
#
# def hello(world):
#     print('Hello %s!' % world)
#
# if __name__ == '__main__':
#     for i in ['1','2','3']:
#         t = threading.Thread(target=hello,args=i)
#         t.start()

# import threading
# import subprocess
#
# class Ping:
#     def __init__(self,host):
#         self.host = host
#     def __call__(self):
#         result = subprocess.run('ping -c2 %s &>/dev/null' % self.host, shell=True)
#         if result.returncode == 0:
#             print('%s up!' % self.host)
#         else:
#             print('%s down!' % self.host)
#
# if __name__ == '__main__':
#     ips = ('172.0.0.%s'% i for i in range(1,255))
#     for i in ips:
#         t = threading.Thread(target=Ping(i))
#         t.start()

# import sys
# from urllib import request
#
# def download(url,fname):
#     html = request.urlopen(url)
#     with open(fname,'wb')as fobj:
#         while 1:
#             data = html.read(4096)
#             if not data:
#                 break
#             fobj.write(data)
#
# if __name__ == '__main__':
#     download(sys.argv[1],sys.argv[2])

import os
import wget
import re

def get_patt(fname,patt,charset=None):
    result = []
    cpatt = re.compile(patt)
    with open(fname,encoding=charset)as fobj:
        print(fobj.read())
        for line in fobj:
            # print(line)
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result

if __name__ == '__main__':
    img_dir = '/tmp/tupian'
    fname163 = '/tmp/tupian/tupian.html'
    url163 = 'https://pic.sogou.com/'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname163):
        wget.download(url163,fname163)

    # img_patt = '(http|https)://[\w./-]+\.(jpg|jpeg|png|gif)'
    img_patt = 'https://img0[0-9].sogoucdn.com/app/a/\w+/\w+'
    img_list = get_patt(fname163, img_patt,'UTF-8')
    print(img_list)

    # for url in img_list:
    #     wget.download(url, img_dir)