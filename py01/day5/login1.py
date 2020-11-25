import getpass
stack = {'tom': '123'}

def register():
    '用于新用户注册'
    o = input("输入用户名")
    i = o in stack
    if i :
        print("用户存在")
    else:+


        p = int(input("输入密码:"))
        stack[o] = p
        print("注册成功")


# print(stack)
def login():
    '用于登陆'
    n = input("输入用户名: ")
    if n :
        p = getpass.getpass("输入密码:").strip()
    i = n in stack
    k = p in stack.values()
    if i and  k:
        print("登录成功")
    else:
        print("用户或密码错误")

def show_menu():
    '程序主体，实现代码逻辑'
    funcs = {'0': register, '1':login}
    prompt = '''(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2):'''
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0','1','2']:
            print("无效的输入，请重试。")
            continue

        if choice == '2':
            print("bye-bye")
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()