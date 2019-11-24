import time
import random

player_victory = 0
enemy_victory = 0

for i in range(1,4):
    time.sleep(1.5)
    print('\nThe %s round' %i)
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)

    print('Player \nlife:%s\nattack:%s' % (player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('enemy\nlife:%s\nattack:%s' % (enemy_life,enemy_attack))
    print('-----------------------')
    time.sleep(1)

    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack 
        enemy_life = enemy_life - player_attack
        print('You are attacking,enemy life is%s' % enemy_life)
        print('Enemy is attacking you,your life is %s' % player_life)
        print('-----------------------')
        time.sleep(1.2)

    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('You win')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('You loose')
    else:
        print('You both loose')

if player_victory > enemy_victory :
    time.sleep(1)
    print('\nFinal result: you win')
elif enemy_victory > player_victory:
    print('\nFinal result: you loose')
else: 
    print('\nFinal result: even')
