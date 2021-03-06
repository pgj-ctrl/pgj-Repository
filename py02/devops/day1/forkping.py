import subprocess
import os
import time

def ping(host):
    k = subprocess.run('ping -c2 %s &> /dev/null' % host,shell=True)
    if k.returncode == 0:
        print('%s is up'% host)
    else:
        print('%s is down'% host)

if __name__ == '__main__':
    ips = ('192.168.1.%s' % i for i in range(1,255))
    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()