class Battle(object):
    def __init__(self):
        pass

    def fight(self, monsters, hero, monster):
        print "Which weapon will you attack with?\n"
        for key in hero.weapons.keys():
            print " * " + key
        weapon = raw_input("\n> ")
        hero.attack_monster(monster, weapon)
        if monster.health <= 0:
            print "You have defeated the %s!\n" % (monster.name)
            hero.xp += monster.xp_value
            del monsters[monsters.index(monster)]
        # hero.check_level()