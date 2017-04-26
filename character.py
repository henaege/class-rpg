from random import randint

class Character(object):
    def __init__(self, name = "Bob"):
        self.name = name
        self.health = 12
        self.power = "1d6"
        self.armor_class = 8
        self.max_health = self.health
        self.xp = 0
        self.level = 1
        self.weapons = {
            'sword': 8,
            'mace': 10,
            'arrow': 6
        }
        self.potions = 3

    def cheer_hero(self):
        print "\n %s Fighting!\n" % self.name

# this class method returns True if hero is alive, False if hero is dead
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
       
    def attack_monster(self, enemy, weapon):
        self.attack = randint(1, 21)
        self.temp_power = (randint(1, self.weapons[weapon])) + 2
        if self.attack == 20:
            print "** Critical Hit!! Double Damage! **\n"
            self.temp_power = self.temp_power * 2
        if enemy.name == "Skeleton" and (weapon == 'sword' or weapon == 'arrow'):
            if self.attack >= enemy.armor_class:
                self.temp_power = self.temp_power / 2
                enemy.health -= self.temp_power
                print "%s strikes the %s with the %s and deals %d damage!\n" % (self.name, enemy.name, weapon, self.temp_power)
                print "The %s now has %d health.\n" % (enemy.name, enemy.health)
            else:
                print "%s missed!\n" % (self.name)
        elif self.attack >= enemy.armor_class:
                enemy.health -= self.temp_power
                print "%s strikes the %s with the %s and deals %d damage!\n" % (self.name, enemy.name, weapon, self.temp_power)
                print "The %s now has %d health.\n" % (enemy.name, enemy.health)
        else:
            print "%s missed!\n" % (self.name)

    def health_boost(self):
        amount = randint(1, 6)
        if self.potions > 0:
            self.health += amount
            print "%s drank a magical potion and gained %d health!\n" % (self.name, amount)
            if self.health > self.max_health:
                self.health = self.max_health
            self.potions -= 1
            print "%s has %d potions left.\n" % (self.name, self.potions)
        else:
            print "No potions left!"

    def enrage(self):
        pass

    def check_level(self):
        if self.xp > 12:
            self.level_up()

    def level_up(self):
        self.max_health += 2
        self.health = self.max_health
        self.temp_power += 1
        print "You Leveled Up!"

class Hero(Character):
    def __init__(self, name):
        super(Hero, self).__init__(name)
        self.name = name
        self.health = 12
        self.power = "1d6"
        self.armor_class = 12
        self.max_health = self.health
        self.xp = 0
        self.level = 1
        self.weapons = self.weapons
        self.potions = 3

class Wizard(Character):
    def __init__(self, name):
        super(Hero, self).__init__(name)
        self.name = name
        self.health = 8
        self.power = "1d4"
        self.armor_class = 10
        self.max_health = self.health
        self.xp = 0
        self.level = 1
        self.weapons = {
            'quarterstaff': 4,
            'dagger': 6
        }
        self.potions = 4
        self.spell_slots = 3
        self.spells = {
            'magic missle': 8,
            'fireball': 12,
            'shield': 6
        }

