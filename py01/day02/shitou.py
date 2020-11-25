import random
#计算机出的和我出的
all_choices = ['石头','剪刀','布']
computer = random.choice(all_choices)
player = input('请选择石头/剪刀/布: ')
#输出计算机的选择和我的选择
print('你出了 %s , 计算机出了 %s' % (player, computer))
#判断输赢
if player == '石头':
    if computer == '石头':
        print('平局')
    elif cpmputer == '剪刀':
        print('You Win !!!')
    else:
        print('You Lose !!!')
elif player == '剪刀':
    if computer =='石头':
        print('You Lose !!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You Win!!!')
else:
    if computer =='石头':
        print('You Win!!!')
    elif cpmputer == '剪刀':
        print('You Lose !!!')
    else:
        print('平局')
