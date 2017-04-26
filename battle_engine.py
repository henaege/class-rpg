class Battle(object):
    def __init__(self):
        pass

    def fight(self, monsters, hero, monster):
        print "Which weapon will you attack with?\n"
        for key in hero.weapons.keys():
            print " * " + key
        weapon = raw_input("\n> ")
        hero.attack_monster(monster, weapon)
        hero.is_alive()
        if monster.health <= 0:
            print "You have defeated the %s!\n" % (monster.name)
            hero.xp += monster.xp_value
            killed = filter(moster.is_alive(), monsters)
        hero.check_level()