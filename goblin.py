from random import randint

class Goblin(object):
    def __init__(self):
        self.name = "Goblin"
        self.health = 8
        self.power = 4
        self.armor_class = 6
        self.xp_value = 5

    def is_alive(self):
        return self.health > 0

    def attack_hero(self, hero):
        self.attack = randint(1, 20)
        self.temp_power = randint(1, 4)
        if self.attack >= hero.armor_class:
            hero.health -= self.temp_power
            print "The goblin hit %s and did %d damage!\n" % (hero.name, self.temp_power)
        else:
            print "The goblin missed its attack!\n"

    def health_boost(self, combatant):
        combatant.health += randint(1, 5)
        print "%s received a magical health boost!" % (combatant.name)
