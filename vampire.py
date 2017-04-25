from random import randint

class Vampire(object):
    def __init__(self):
        self.health = 12
        self.power = 8
        self.armor_class = 12
        self.name = "Vampire"
        self.xp_value = 10

    def is_alive(self):
        return self.health > 0

    def attack_hero(self, hero):
        self.attack = randint(1, 20)
        self.temp_power = randint(1, 8)
        if self.attack >= hero.armor_class:
            hero.health -= self.temp_power
            print "The %s hit %s and did %d damage!\n" % (self.name, hero.name, self.temp_power)
        else:
            print "The %s missed its attack!\n" % (self.name)