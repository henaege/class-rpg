from random import randint
class Skeleton(object):
    def __init__(self):
        self.health = 13
        self.power = 6
        self.armor_class = 13
        self.name = "Skeleton"
        self.xp_value = 8

    def is_alive(self):
        return self.health > 0

    def attack_hero(self, hero):
        self.attack = randint(1, 20)
        self.temp_power = (randint(1, 7) + 2)
        print "The Skeleton is attacking!\n"
        if self.attack >= hero.armor_class:
            hero.health -= self.temp_power
            print "The %s hit %s and did %d damage!\n" % (self.name, hero.name, self.temp_power)
        else:
            print "The %s missed its attack!\n" % (self.name)