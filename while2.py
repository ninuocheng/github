import random
choices = ['石头','剪刀','布']

# player = input('请出拳(石头/剪刀/布):')
prompt = '''(0)石头
(1)剪刀
(2)布
请选择(0/1/2):'''

win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
pwin = 0
cwin = 0
while 1:
    computer = random.choice(choices)
    ind = int(input(prompt))
    player = choices[ind]
    print('Your choice:%s,couputer choice:%s' % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou Lose!!!\033[0m')
    if pwin == 2 or cwin == 2:
        break