# this is a procedural approach to a text-based RPG game.
# THe hero is fighting a goblin. has the option to:
# 1. fight
# 2. do nothing(the goblin will still attack)
# 3. Run

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    # Run game as long as both characters have health
    while goblin_health > 0 and hero_health > 0:
        print("You have %d health and %d power.\n" % (hero_health, hero_power))
        print ("The goblin has %d health and %d power.\n" % (goblin_health, goblin_power))
        print ("What do you want to do?\n")
        print ("1. fight goblin\n")
        print ("2. do nothing\n")
        print ("3. flee\n")
        print ("> ",)
        user_input = input()
        if user_input == "1":
            goblin_health -= hero_power
            print ("You have done %d damage to the goblin\n" % (hero_power))
            if goblin_health <= 0:
                print ("You have defeated the goblin\n")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print ("Goodbye, Coward!")
            break
        else:
            print ("Invalid input %s" % (user_input))

        if goblin_health > 0:
            # hero has attacked(or not) and goblin is still alive
            hero_health -= goblin_power
            print ("The goblin hits you for %d damage\n" % (goblin_power))
            if hero_health <= 0:
                print ("You have been killed by a goblin.\n")

        if hero_health > 0 and hero_health < 5:
            print ("You have gone into a rage! Your power has increased!\n")
            hero_power += 5

main()