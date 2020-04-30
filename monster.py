from random import randint

class Monster(object):
    def __init__(self, name):
        self.name = name
        self.health = 8
        self.power = 4
        self.armor_class = 6
        self.xp_value = 5

    def __repr__(self):
        return '' % (self.name)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack_hero(self, hero):
        self.attack = randint(1, 20)
        self.temp_power = randint(1, 5)
        print("The %s is attacking %s!\n" % (self.name, hero.name))
        if self.attack >= hero.armor_class:
            hero.health -= self.temp_power
            print("The %s hit %s and did %d damage!\n" % (self.name, hero.name, self.temp_power))
            print("%s now has %d health.\n" % (hero.name, hero.health))
            if hero.health <= 0:
                return hero.is_alive()
        else:
            print("The %s missed its attack!\n" % (self.name))

class Goblin(Monster):
    def __init__(self):
        super(Goblin, self).__init__("Goblin")
        self.health = randint(2, 9)
        self.power = randint(2, 5)
        self.armor_class = 6
        self.xp_value = 5

    def __repr__(self):
        return self.name

class Vampire(Monster):
    def __init__(self):
        super(Vampire, self).__init__("Vampire")
        self.health = randint(6, 13)
        self.power = randint(4, 9)
        self.armor_class = 12
        self.xp_value = 10

    def __repr__(self):
        return self.name

class Skeleton(Monster):
    def __init__(self):
        super(Skeleton, self).__init__("Skeleton")
        self.health = randint(3, 13)
        self.power = randint(2, 7)
        self.armor_class = 13
        self.xp_value = 8

    def __repr__(self):
        return self.name
