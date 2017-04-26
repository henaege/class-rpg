from random import randint
import pygame

# import the Hero class from hero.py
from hero import Hero
# import the Goblin class from goblin.py
from monster import *
# from goblin import Goblin
# from vampire import Vampire
# from skeleton import Skeleton
from battle_engine import Battle
# from get_monsters import GetMonsters

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("./sounds/battle.ogg")
pygame.mixer.music.play(-1)

the_hero = Hero(raw_input("\nWhat is thy name, brave adventurer? "))
number_of_enemies = int(raw_input("\nHow many monsters can you fight? "))
the_hero.cheer_hero()

monsters = []

for i in range(0, number_of_enemies):
            monster_list = [Goblin(), Vampire(), Skeleton()]
            list_index = randint(0, len(monster_list)-1)
            monsters.append(monster_list[list_index])

# the_hero.is_alive()
# print monsters

#  Run game as long as both characters have health
def main():
    while the_hero.is_alive():
        # the_hero = Hero(raw_input("\nWhat is thy name, brave adventurer? "))
        # number_of_enemies = int(raw_input("\nHow many monsters can you fight? "))
        # the_hero.cheer_hero()
        the_hero.health = 12
        if len(monsters) == 0:
            for i in range(0, number_of_enemies):
                monster_list = [Goblin(), Vampire(), Skeleton()]
                list_index = randint(0, len(monster_list)-1)
                monsters.append(monster_list[list_index])
        for monster in monsters:
            print monsters
            print "%s has encountered a %s.\n" % (the_hero.name, monster.name)
            print "%s has %d health and armor class %d.\n" % (the_hero.name, the_hero.health, the_hero.armor_class)
            print "The %s has %d health, %d power and armor class %d.\n" % (monster.name, monster.health, monster.power, monster.armor_class)
            print "What will %s do?\n" % (the_hero.name)
            print "1. Fight %s\n" % (monster.name)
            print "2. Do Nothing\n"
            print "3. Flee\n"
            print "4. Drink Health Potion\n"
            print "> "
            user_input = raw_input()
            if user_input == "1":
                while monster.health > 0:
                    if the_hero.health < 5 and the_hero.potions > 0:
                        drink_potion = raw_input(the_hero.name + 
    """'s health is getting low. Maybe a potion would help?
    1. Drink Potion
    2. Take it like a man\n
    > """)
                        if drink_potion == "1":
                            if the_hero.potions < 1:
                                print "No more potions!"
                            the_hero.health_boost()
                        else:
                            print "The situation looks dire...\n"
                    
                    encounter = Battle()
                    encounter.fight(monsters, the_hero, monster)
                    if monster.health > 0:
                    # hero has attacked(or not) and goblin is still alive
                        monster.attack_hero(the_hero)
                    if the_hero.health <= 0:
                        print "%s was killed by the %s. the quest is over.\nFarewell." % (the_hero.name, monster.name)
                        return

                    
            elif user_input == "2":
                pass
            elif user_input == "3":
                print "\n %s runs away like a sissy!\n" % (the_hero.name)
                return
            elif user_input == "4":
                the_hero.health_boost()
            else:
                print "Invalid input %s" % (user_input)

        if len(monsters) < 1:
            fight_more = raw_input("There are no monsters left! Would %s like to fight more (Y / N)? " % (the_hero.name)) 
            if fight_more.upper() == "Y":
                continue
            if fight_more.upper() == "N":
                print "Goodbye, wimp!"
                return
                

            
        

                        


            # if the_hero.is_alive() and the_hero.health < 5:
            #     print "You have gone into a rage! Your power has increased!\n"
            #     the_hero.temp_power += 5
            
                

            

main()