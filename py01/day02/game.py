import random
#计算机出的和我出的
all_choices = ['石头', '剪刀', '布']
computer = random.choice(all_choices)
player = input('请选择石头/剪刀/布: ')
#定义玩家赢的情况
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
#输出计算机的选择和我的选择
print('你出了 %s , 计算机出了 %s' % (player , computer))
#判断输赢
if player == computer:
    print('平局')
elif [player,computer] in win_list:
    print('You WIN ！！！')
else:
    print('You Lose ！！！')