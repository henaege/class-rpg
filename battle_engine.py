from random import randint

class Battle(object):
    def __init__(self):
        pass

    def fight(self, monsters, hero, wizard, monster):
        heroes = []
        for i in range(0, 2):
            hero_list = [hero, wizard]
            list_index = randint(0, len(hero_list)-1)
            heroes.append(hero_list[list_index])
        print "Which weapon will %s attack with?\n" % (hero.name)
        for key in hero.weapons.keys():
            print " * " + key
        weapon = raw_input("\n> ")
        hero.attack_monster(monster, weapon)
        if monster.health <= 0:
            print "You have defeated the %s!\n" % (monster.name)
            hero.xp += monster.xp_value
            del monsters[monsters.index(monster)]
            return
        if monster.health > 0:
                    # hero has attacked(or not) and goblin is still alive
            for attacked_hero in heroes:
                monster.attack_hero(attacked_hero)
                if attacked_hero.health <= 0:
                    del heroes[heroes.index(attacked_hero)]
                    return
        attack_mode = raw_input("""How will %s attack?\n
        1. Weapon
        2. Spell 
        > """ % (wizard.name))
        if attack_mode == '1':
            print "Which weapon will %s attack with?\n" % (wizard.name)
            for key in wizard.weapons.keys():
                print " * " + key
            weapon = raw_input("\n> ")
            wizard.attack_monster(monster, weapon)
        elif attack_mode == '2':    
            for key in wizard.spells.keys():
                print " * " + key
            spell = raw_input("\n> ")
            wizard.cast_spell(spell, monster)
        else:
            print "Please enter a valid choice (1 or 2)."
        # if monster.health > 0:
        #             # hero has attacked(or not) and goblin is still alive
        #     monster.attack_hero(hero)
            # if hero.health <= 0:
           #     return hero.is_alive()
        if monster.health <= 0:
            print "You have defeated the %s!\n" % (monster.name)
            hero.xp += monster.xp_value
            del monsters[monsters.index(monster)]

        
        # hero.check_level()