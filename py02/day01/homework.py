import time
u = time.strftime('%Y-%m-%d')


def push_it():
    data = [['2020-7-21', 0, 0, 10000, 'init data']]
    q = data[-1][-2]
    init_data = []
    t = int(input("入账/出账多少钱:").strip())
    d = q + t
    r = input("原因")
    for i in [u,t,d,r]:
        init_data.append(i)
    data.append(init_data)
    return data



def view():
    print('05246')
def show_mune():
    port = """(0)入账/出账
(1)查询
(2)退出
请选择0/1/2/:"""
    funs = {'0':push_it,'1':view}
    while 1:
        y = input(port).strip()
        if y not in ['0','1','2',]:
            print('无效输入')
            continue
        if y == '2':
            print("Bye-bye")
            break
        funs[y]()
if __name__ == '__main__':
    show_mune()