# all_table = {}
#
# def select():
#     while 1:
#         n = input("输入账号: ")
#         if n:
#             p = print("输入密码: ")
#         else:
#             print("账号不能为空")
#         if n in all_table and p in all_table.values():
#             print("登录成功")
#
#
#
#
# if __name__ == '__main__':
#     select()
import getpass
userdb = {}
import getpass

def register():
    '用于新用户注册'
    username = input("username:").strip()
    if username == '':
        print("用户名不能为空")
    elif username in userdb:
        print("用户已存在。")
    else:
        password = input("password")
        userdb[username] = password

def login():
    '用于登陆'
    username = input("username:")
    password = getpass.getpass("password")
    if userdb.get(username) == password:
        print("登陆成功")
    else:
        print("登陆失败")

def show_menu():
    '程序主体，实现代码逻辑'
    funcs = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print("无效的输入，请重试。")
            continue

        if choice == '2':
            print('Bye-bye')
            break

        funcs[choice]()

if __name__ == '__main__':
    show_menu()