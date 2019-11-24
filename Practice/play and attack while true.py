import time, random
i =1
player_v=0
enemy_v=0
while True:
    player_l=random.randint(100,150)
    player_a=random.randint(30,50)
    enemy_l=random.randint(100,150)
    enemy_a=random.randint(30,50)
    print('this is the %s round'% i )
    print('player is life is %s, attack is %s' %(player_l, player_a))
    print('\nenemy is life is %s, attack is %s' %(enemy_l,enemy_a))
    time.sleep(1)
    while player_l>0 and enemy_l>0:
        player_l=player_l-enemy_a
        enemy_l=enemy_l-player_a
        print('\nplayer life is %s, enemy life is %s' %(player_l,enemy_l))
        time.sleep(1)
    if player_l>0 and enemy_l<=0:
        player_v +=1
        print('\nplayer win')
    elif player_l<=0 and enemy_l>0:
        enemy_v +=1
        print('\nPlayer lose')
    else:
        print('\nyou both lose')
    i +=1
    a1 = input('\nDo you want to continue?:')
    if a1 == 'n':
        break
if player_v>enemy_v:
    print('\nFinal result: player win')
elif player_v<enemy_v:
    print('\nFianl result: player lose')
else:
    print('\nFinal result: even')