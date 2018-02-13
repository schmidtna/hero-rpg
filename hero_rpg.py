#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, race, health, power):
        self.health = health
        self.power = power
        self.name = name
        self.race = race

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
    
        enemy.health -= self.power
        print("{} does {} damage to {} the {}.".format(self.name, self.power, enemy.name, enemy.race))
        if enemy.health <= 0:
            print("{} the {} is dead.".format(enemy.name, enemy.race))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    pass
    
class Goblin(Character):
    pass
    
    


hero = Hero("Kyle", "human", 10, 5)
goblin = Goblin("Gornak", "goblin", 6, 2)



def main():
   
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
main()





