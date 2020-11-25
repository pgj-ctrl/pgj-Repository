import random

all_choices = ['石头', '剪刀', '布']
prompt = '''(0)石头
(1)剪刀
(2)布
请选择(0/1/2/)'''
pwin = 0
cwin = 0
while 1:
    if pwin == 2 or cwin == 2:
        break

    ind = int(input(prompt))
    player = all_choices[ind]
    computer = random.choice(all_choices)
    win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
    print('你出了 %s , 计算机出了 %s' % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        print('\033[33;1mYou WIN ！！！\033[0m')
        pwin += 1
    else:
        print('\033[31;1mYou Lose ！！！\033[0m')
        cwin += 1