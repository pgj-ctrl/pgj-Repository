a = int(input("number: "))

if 90<= a <= 99:
    print("优秀")
elif 80 <= a < 90:
    print("好")
elif 70 <= a < 80:
    print("良")
elif 60<= a < 70:
    print("及格")
elif a == 100:
    print("满分天才")
elif a > 100:
    print("满分100没有超出100的")
elif a < 0:
    print("试卷最低零分没有负数")
else:
    print("你要努力了")




