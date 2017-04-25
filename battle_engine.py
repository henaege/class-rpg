class Battle(object):
    def __init__(self):
        pass

    def fight(self):
        print "Which weapon will you attack with?\n"
        for key in the_hero.weapons.keys():
            print " * " + key
        weapon = raw_input("\n> ")
        the_hero.attack_monster(monster, weapon)
        if monster.health <= 0:
            print "You have defeated the %s!\n" % (monster.name)
            the_hero.xp += monster.xp_value
            the_hero.check_level()