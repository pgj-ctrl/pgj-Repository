import time
import pickle
import os
t = time.strftime('%Y-%m-%d')

data = []
def save():
    try:
        m = int(input("输入收入").strip())
    except (ValueError)as e:
        print("请输入数字",e)
    else:
        r = input("原因")

def cost():
    print("lll")

def query():
    print("wasdf")

def show_menu():
    funs = {'0':save ,'1':cost,'2':query}
    prompt = """（0）收入
（1）开销
（2）查询
（3）退出
请选择0/1/2/3/:"""
    fname = "account.data"
    #如果记账文件不存在需要初始化它
    if not os.path.exists(fname):
        init_data= [[t],0,0,10000,'init data']
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)
    while 1:
        u = input(prompt).strip()
        if u not in ['0','1','2','3']:
            print("无效输入")
            continue
        if u == '3':
            print("Bye-bye")
            break
        funs[u]()


if __name__ == '__main__':
        show_menu()