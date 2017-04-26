from random import randint
from monster import Monster



class Goblin(Monster):
    def __init__(self):
        super(Goblin, self).__init__("Goblin")
        self.health = randint(2, 9)
        self.power = randint(2, 5)
        self.armor_class = 6
        self.xp_value = 5

    def __repr__(self):
        return self.name

