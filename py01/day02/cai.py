import random
number = random.randint(1,100)

cwin = 0
i = 1
while i < 7:
    i += 1
    number2 = int(input('输入你猜的数字，1~100: '))
    if number2 > number:
        print('猜大了')
    elif number2 < number:
        print('猜小了')
    else:
        print('猜对了')
        break
else:
    print('number is ',number)