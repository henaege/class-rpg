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
        weapon = ""
        weapon_choice = False
        while not weapon_choice:
            print("Which weapon will %s attack with?\n" % (hero.name))
            for key in hero.weapons.keys():
                print(" * " + key)

            weapon = input("\n> ")
            if weapon in hero.weapons:
                weapon_choice = True
            elif weapon == "1":
                weapon = "sword"
                weapon_choice = True
            elif weapon == "2":
                weapon = "mace"
                weapon_choice = True
            elif weapon == "3":
                weapon = "arrow"
                weapon_choice = True
            elif weapon != ("sword" or "mace" or "arrow"):
                print("Try again...\n")
            else:
                weapon_choice = True
        hero.attack_monster(monster, weapon)
        if monster.health <= 0:
            print("You have defeated the %s!\n" % monster.name)
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
        attack_mode = input("""How will %s attack?\n
        1. Weapon
        2. Spell 
        > """ % wizard.name)
        if attack_mode == '1':
            wiz_weapon = ""
            wiz_weapon_choice = False
            while not wiz_weapon_choice:
                print("Which weapon will %s attack with?\n" % wizard.name)
                for key in wizard.weapons.keys():
                    print(" * " + key)
                wiz_weapon = input("\n> ")
                if wiz_weapon in wizard.weapons:
                    wiz_weapon_choice = True
                elif wiz_weapon == "1":
                    wiz_weapon = "quarterstaff"
                    wiz_weapon_choice = True
                elif wiz_weapon == "2":
                    wiz_weapon = "dagger"
                    wiz_weapon_choice = True
                elif wiz_weapon != ("quarterstaff" or "dagger"):
                    print("Try again...\n")
                else:
                    wiz_weapon_choice = True
            wizard.attack_monster(monster, wiz_weapon)
        elif attack_mode == '2':
            spell = ""
            spell_choice = False
            while not spell_choice:
                for key in wizard.spells.keys():
                    print(" * " + key)
                spell = input("\n> ")
                if spell in wizard.spells:
                    spell_choice = True
                elif spell == "1":
                    spell = "magic missile"
                    spell_choice = True
                elif spell == "2":
                    spell = "fireball"
                    spell_choice = True
                elif spell == "3":
                    spell = "shield"
                    spell_choice = True
                elif spell != ("magic missile" or "fireball" or"shield"):
                    print("Try again...\n")
                else:
                    spell_choice = True
            wizard.cast_spell(spell, monster)
        else:
            print("Please enter a valid choice (1 or 2).")
        # if monster.health > 0:
        #             # hero has attacked(or not) and goblin is still alive
        #     monster.attack_hero(hero)
            # if hero.health <= 0:
           #     return hero.is_alive()
        if monster.health <= 0:
            print("You have defeated the %s!\n" % monster.name)
            hero.xp += monster.xp_value
            del monsters[monsters.index(monster)]

        
        # hero.check_level()