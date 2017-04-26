from random import randint
class Skeleton(object):
    def __init__(self):
        self.health = 13
        self.power = 6
        self.armor_class = 13
        self.name = "Skeleton"
        self.xp_value = 8

    def __repr__(self):
        return self.name

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack_hero(self, hero):
        self.attack = randint(1, 19)
        self.temp_power = (randint(1, 7) + 2)
        print "The Skeleton is attacking!\n"
        if self.attack >= hero.armor_class:
            hero.health -= self.temp_power
            print "The %s hit %s and did %d damage!\n" % (self.name, hero.name, self.temp_power)
            print "%s now has %d health.\n" % (hero.name, hero.health)
            if hero.health <= 0:
                print """%s has been killed by a %s.\nthe quest has failed.""" % (hero.name, self.name)
        else:
            print "The %s missed its attack!\n" % (self.name)