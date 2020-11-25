stack = []

def push_it():
    "用于压栈"
    data = input("数据:>").strip()
    if  data:
        stack.append(data)
    else:
        print("\033[31;1m没有获取到数据\033[0m")

def pop_it():
    "用于出栈"
    if stack:
        data = stack.pop()
        print("从栈中弹出了: \033[31;1m%s\033[0m" % data)
    else:
        print("\033[31;1m栈已经为空\033[0m")

def view():
    "查询"
    print("\033[32;1m%s\033[0m" % stack)

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