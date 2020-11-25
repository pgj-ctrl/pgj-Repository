# stack = []
# def push_it():
#     "用于压栈"
#     data = input("数据:>")
#     if data:
#         stack.append(data)
#     else:
#         print("没有获取到数据")
#
# def pop_it():
#     "用于出栈"
#     if stack:
#         data = stack.pop()
#         print("从栈中弹出了:%s" % data)
#     else:
#         print("栈已经为空")
#
# def view():
#     "查询"
#     print(stack)
# def show_menu():
#     "用于显示菜单，实现代码逻辑"
#     prompt = '''(0) 压栈
# (1) 出栈
# (2) 查询
# (3) 退出
# 请选择(0/1/2/3): '''
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print("无效的输入，请重试")
#             continue
#         if choice == '3':
#             print("Bye-bye")
#             break
#         if choice == '0':
#             push_it()
#         elif choice == '1':
#             pop_it()
#         else:
#             view()
#
# if __name__ == '__main__':
#     show_menu()

# stack = []
#
# def push_it():
#     while 1:
#         n = input("请输入内容")
#         if n :
#             stack.append(n)
#             break
#         else:
#             print("内容不能为空")
#
#
# def pop_it():
#     print("出栈了",stack.pop())
#
#
# def view():
#     print(stack)
#
#
# def show_menu():
#     pormpt = """(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3): """
#     while 1:
#         choice = input(pormpt).strip()
#         if choice not in ['0','1','2','3']:
#             print("无效的输入，请重试")
#             continue
#         if choice == '3':
#             print("Bye-bye")
#             break
#         if choice == '0':
#             push_it()
#         elif choice == '1':
#             pop_it()
#         else:
#             view()
#
# if __name__ == '__main__':
#     show_menu()

# stack= []
#
# def push_it():
#     data = input("数据:>").strip()
#     if data:
#         stack.append(data)
#     else:
#         print("\033[31;1m没有获取到数据\033[0m")
#
# def pop_it():
#     "用于出栈"
#     if stack:
#         data = stack.pop()
#         print("从栈中弹出了: \033[31;1m%s\033[0m" % data)
#     else:
#         print("\033[31;1m栈已经为空\033[0m")
#
# def view():
#     "查询"
#     print("\033[32;1m%s\033[0m" % stack)
#
# def show_menu():
#     "用于显示菜单，实现代码逻辑"
#     funcs = {'0': push_it, '1': pop_it,'2':view}
#     prompt = """(0)压栈
# (1) 出栈
# (2) 查询
# (3) quit
# 请选择(0/1/2/3): """
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print("无效的输入，请重试。")
#             continue
#
#         if choice == '3':
#             print('Bye-bye')
#             break
#
#         funcs[choice]()
#
# if __name__ == '__main__':
#     show_menu()