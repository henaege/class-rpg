from random import randint

# import the Hero class from hero.py
from hero import Hero
# import the Goblin class from goblin.py
from goblin import Goblin
from vampire import Vampire
from skeleton import Skeleton
from battle_engine import Battle

the_hero = Hero(raw_input("\nWhat is thy name, brave adventurer? "))
number_of_enemies = int(raw_input("\nHow many monsters can you fight? "))
the_hero.cheer_hero()
monster_list = [Goblin(), Vampire(), Skeleton()]
monsters = []

for i in range(0, number_of_enemies):
    list_index = randint(0, len(monster_list)-1)
    monsters.append(monster_list[list_index])


# monster_list = random.shuffle(monsters)
# print monsters
# number_of_enemies = raw_input("How many goblins can you fight? ")
#  Run game as long as both characters have health
def main():
   
    for monster in monsters:
        print "You have encountered a %s.\n" % (monster.name)          
        while monster.health > 0 and the_hero.is_alive():
            print "You have %d health and a %d armor class.\n" % (the_hero.health, the_hero.armor_class)
            print "The %s has %d health, %d power and a %d armor class.\n" % (monster.name, monster.health, monster.power, monster.armor_class)
            print "What do you want to do?\n"
            print "1. Fight %s\n" % (monster.name)
            print "2. Do Nothing\n"
            print "3. Flee\n"
            print "4. Drink Health Potion\n"
            print "> "
            user_input = raw_input()
            if user_input == "1":
                print "Which weapon will you attack with?\n"
                for key in the_hero.weapons.keys():
                    print " * " + key
                weapon = raw_input("\n> ")
                the_hero.attack_monster(monster, weapon)
                if monster.health <= 0:
                    print "You have defeated the %s!\n" % (monster.name)
                    the_hero.xp += monster.xp_value
                    the_hero.check_level()
            elif user_input == "2":
                pass
            elif user_input == "3":
                print "%s runs away like a sissy!\n" % (the_hero.name)
                break
            elif user_input == "4":
                the_hero.health_boost()
            else:
                print "Invalid input %s" % (user_input)

            if monster.health > 0:
                    # hero has attacked(or not) and goblin is still alive
                monster.attack_hero(the_hero)
                if the_hero.health <= 0:
                    print """You have been killed by a %s.\nYou have failed your quest.""" % (monster.name)
                    

                        


            # if the_hero.is_alive() and the_hero.health < 5:
            #     print "You have gone into a rage! Your power has increased!\n"
            #     the_hero.temp_power += 5
            
                

            

main()