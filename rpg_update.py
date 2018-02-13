
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
    