#-*-coding:utf-8-*-
import random

player_hp = 260
# enemy_atk = {'min': 10, 'max':50}

class Enemy:
    hp = 200

    def __init__(self, atk_min, atk_max):
        # set obj with instance
        self.atk = {'min':atk_min, 'atk_max':atk_max}

    def get_atk(self):
        print(self.atk['min'])

    def get_hp(self):
        print("Hp is:", self.hp)

enemy1 = Enemy(20, 50)
enemy1.get_atk()
enemy1.get_hp()

enemy2 = Enemy(16, 31)
enemy2.get_atk()
enemy1.get_hp()



'''
while player_hp > 0:
    damage = random.randrange(enemy_atk['min'], enemy_atk['max'])
    player_hp -= damage

    if player_hp <= 30:
        pass
        # player_hp = 30

    print("enemy strikes for", damage, "points of damage, Current HP is", player_hp)

    if player_hp > 30:
        continue

    print(' -> You have low health, You\'ve been teleported the nearest inn')
    break
'''