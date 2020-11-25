# def push_it():
#     "用于压栈"
#
#
# def pop_it():
#     "用于出栈"
#
#
# def view():
#     "查询"
#
#
# def show_menu():
#
# if __name__ == '__main__':
#     show_menu()
#
#
#
#
#
#     "用于显示菜单，实现代码逻辑"
#     n = print("""(0) 压栈
# (1) 出栈
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3):""")
#     if n == 0:
#         push_it()
#     elif n == 1:
#         pop_it()
#     elif n == 2:
#         view()
#     else:
#        if n not in ['0','1','2','3']:
#            print("无效的输入，请重试")
#        else:
#            break

def push_it():
    "用于压栈"
    r = []
    p = input("请输入内容：")
    r.append(p)
    return r
    # print(r)

def pop_it(value):
    "用于出栈"
    name = value
    name.pop()

def view():
    "查询"


def show_menu():
    "用于显示菜单，实现代码逻辑"
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3):"""
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0','1','2','3']:
            print("无效的输入，请重试")
            continue
        if choice == '3':
            print("bye-bye")
            break
        if choice == "0":
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view()
if __name__ == '__main__':
    show_menu()