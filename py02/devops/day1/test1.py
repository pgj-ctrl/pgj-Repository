# import paramiko
# def rcmd(host,user,passwd,port=22,cmds=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host,port=port,username=user,password=passwd)
#     stdin,stdout,stderr = ssh.exec_command(cmds)
#     out  = stdout.read()
#     err = stderr.read()
#     if out:
#         print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
#     if err:
#         print('[%s] \033[31;1mERROR\033[0m:\n%s' %(host, err.decode()))
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('127.0.0.1', 'root', 'redhat', 22, 'id root; id alice')
# import paramiko
#
# def rcmd(host, user, passwd, port=22, cmds=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host, port=port, username=user, password=passwd)
#     stdin, stdout, stderr = ssh.exec_command(cmds)
#     out = stdout.read()
#     err = stderr.read()
#     if out:
#         print("[%s] \033[32;1mOUT\033[0m:\n%s" % (host, out.decode()))
#     if err:
#         print("[%s] \033[31;1mERROR\033[0m:\n%s" % (host, err.decode()))
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('127.0.0.1', 'root', '123', 22, 'id root; id alice')

# import  re
# def count_patt(fname,patt):
#     result = {}
#     cpatt = re.compile(patt)
#
#     with open(fname) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 key = m.group()
#                 result[key] = result.get(key,0)+1
#     return result
#
#
# if __name__ == '__main__':
#     fname= 'access_log'
#     ip = '^(\d+\.){3}\d+'
#     br = 'Chrome|MISE|Firefox'
#     result1 = count_patt(fname,ip)
#     result2 = count_patt(fname,br)
#     print(result1)
#     print(result2)

# import  re
# class Countpatt:
#     def count_patt(self,fname,patt):
#         result = {}
#         cpatt = re.compile(patt)
#         with open(fname)as fobj:
#             for line in fobj:
#                 m = cpatt.search(line)
#                 if m:
#                     key = m.group()
#                     result[key] = result.get(key,0)+1
#         return result
#
# if __name__ == '__main__':
#     fname  = 'access_log'
#     ip = '^(\d+\.){3}\d+'
#     br = 'Chrome|MSIE|Firefox'
#     cp1 = Countpatt()
#     result1 = cp1.count_patt(fname,ip)
#     result2 = cp1.count_patt(fname,br)
#     print(result1)
#     print(result2)

# import re
# class CountPatt:
#     def __init__(self,fname):
#         self.fname = fname
#
#     def count_patt(self,patt):
#         result = {}
#         cpatt = re.compile(patt)
#         with open(self.fname)as fobj:
#             for line in fobj:
#                 m = cpatt.search(line)
#                 if m:
#                     key = m.group()
#                     result[key] = result.get(key,0)+1
#         return result
#
# if __name__ == '__main__':
#     fname = 'access_log'
#     ip = '^(\d+\.){3}\d+'
#     br = 'Chrome|MSIE|Firefox'
#     cp1 =CountPatt(fname)
#     result1 = cp1.count_patt(ip)
#     result2 = cp1.count_patt(br)
#     print(result1)
#     print(result2)

# import hashlib
# import tarfile
# import os
# from time import strftime
# import pickle
#
# def check_md5(fname):
#     m = hashlib.md5()
#     with open(fname,'rb')as fobj:
#         while 1 :
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()
#
# def full_backup(src,dst,md5file):
#     "完全备份"
#     fname = '%s_full_%s.tar.gz'% (os.path.basename(src), strftime("%Y%m%d"))
#     fname = os.path.join(dst,fname)
#
#     tar = tarfile.open(fname,'w:gz')
#     tar.add(src)
#     tar.close()
#
#     md5dict = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     with open(md5file,'wb')as fobj:
#         pickle.dump(md5dict,fobj)
#
# def incr_backup(src,dst,md5file):
#     "增量备份"
#     fname = "%s_incr_%s.tar.gz" % (os.path.basename(src), strftime("%Y%m%d"))
#     fname = os.path.join(dst,fname)
#
#     md5dict = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     with open(md5file,'rb')as fobj:
#         old_md5 = pickle.load(fobj)
#
#     tar = tarfile.open(fname,'w:gz')
#     for key in md5dict:
#         if old_md5.get(key) != md5dict[key]:
#             tar.add(key)
#     tar.close()
#
#     with open(md5file,'wb')as fobj:
#         pickle.dump(md5dict,fobj)
#
# if __name__ == '__main__':
#     src = '/tmp/demo/security'
#     dst = '/tmp/demo/backup'
#     md5file = '/tmp/demo/backup/md5.data'
#     if strftime("%a") == 'Mon' or not os.path.exists(md5file):
#         full_backup(src,dst,md5file)
#     else:
#         incr_backup(src,dst,md5file)

# import os
# import pickle
# from time import strftime
# def save(fname):
#     "用于记录收入"
#     try:
#         amount  = int(input("金额：").strip())
#         comment = input("备注")
#     except(KeyboardInterrupt,EOFError):
#         print('\nBye-bye')
#         exit(1)
#     except ValueError:
#         print("无效的金额")
#         return
#
#     date = strftime("%Y-%m-%d")
#     with open(fname,'rb')as fobj:
#         records = pickle.load(fobj)
#     balance = records[-1][-2] + amout
#
#     record = [ date,amount,0,balance,comment]
#     records.append(record)
#     with open(fname,'wb')as fobj:
#         pickle.dump(records,fobj)
# def cost(fname):
#     "用于记录开销"
#     try:
#         amount = int(input("金额: "))
#         comment  = input("备注: ")
#     except (KeyboardInterrupt,EOFError):
#         print("\nBye-bye")
#         exit(1)
#     except ValueError:
#         print("无效的金额")
#         return
#
#     date = strftime("%Y-%m-%d")
#
#     with open(fname,'rb')as fobj:
#         records = pickle.load(fobj)
#     balance = records[-1][-2] - amount
#
#     record = [date,0,amount,balance,comment]
#     records.append(record)
#     with open(fname,'wb')as fobj:
#         pickle.dump(records,fobj)
#
#
# def query(fname):
#     "用于查询收支情况"
#     print('query')
#
#     print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
#
#     with open(fname,'rb')as fobj:
#         records = pickle.load(fobj)
#     for record in records:
#         print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))
# def show_menu():
#     "主程序代码逻辑"
#     funcs = {'0':save,'1':cost,'2':query}
#     prompt = """(0) 收入
# (1) 开销
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3): """
#     fname = 'account.data'
#     if not os.path.exists(fname):
#         init_data = [[strftime("%Y-%m-%d"), 0, 0, 10000, "init data"]]
#         with open(fname,'wb')as fobj:
#             pickle.dump(init_data,fobj)
#     while 1 :
#         try:
#             choices = input(prompt).strip()
#         except(KeyboardInterrupt,EOFError):
#             choices = '3'
#
#         if  choices not in ['0','1','2','3']:
#             print('无效的输入，请重试。')
#             continue
#
#         if choices == '3':
#             print('\nBye-bye')
#             break
#
#         funcs[choices](fname)
#
# if __name__ == '__main__':
#     show_menu()

from random import randint,choices

def add(x,y):
    return x + y
def sub(x,y):
    return x + y

def exam():
    "出题，用户作答"
    funcs = {'+':add,'-':sub}
    nums = [randint(1,100)for i in range(2)]
    nums.sort(reverse=True)

    op = choices('+-')

    result = funcs[op](*nums)

    i = 0
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    while i < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer == result:
            print("不错哟～")
            break
        print("不对哟～")
        i += 1
    else:
        print("正确答案是：\n%s%s" % (prompt, result))

def main():
    "主程序代码逻辑"
    while 1:
        exam()
        try:
            yn = input("Continue(Y/n)? ").strip()[0]
        except (KeyboardInterrupt,EOFError):
            yn = 'n'
        except IndexError:
            continue
        if yn in 'nN':
            print('\nBye-bye')
            break
if __name__ == '__main__':
    main()