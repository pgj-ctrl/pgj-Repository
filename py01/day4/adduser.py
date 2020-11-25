import sys
import hh
import subprocess

def adduser(user,passwd,fname):
    result = subprocess.run('id %s &> /dev/null' % user, shell = True)
    if result.returncode == 0:
        prin("用户已存在")
        exit(1)

    subprocess.run('useradd %s' % user,shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd,user),shell =True)
    info = """username:%s
password:%s
"""%(user,passwd)
    with open(fname,'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    password = hh.mk_pwd()
    adduser(user,password,fname)