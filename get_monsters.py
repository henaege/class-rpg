from random import randint

class GetMonsters(object):
    def __init__(self):
        pass

    def get_monsters(self, enemies, monster_list):
        monsters = []
        for i in range(0, enemies):
            list_index = randint(0, len(monster_list)-1)
            monsters.append(monster_list[list_index])
            