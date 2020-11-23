# Constructor
import random
from random import choice 
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        players = [self, opponent]
        winner = (choice(players))

        print(f'{winner.name} won!')

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def attack(self):
        ''' Calculates the total damage from all ability attacks. 
        return: total_damage:Int '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object '''
        #This is identical to attack
        total_protection = 0
        for armor in self.armors:
            total_protection += armor.add_armor()
        return total_protection

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks
        return: total_block:Int'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return damage_amt - total_block
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense '''
        self.current_health -= self.defend(damage)
        
    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health <= 0:
            print("Your Hero is dead")
            return False
        else:
            print("Your Hero is alive for now")
            return True

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in'''
        


if __name__=="__main__": 
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(150000)
    print(hero.is_alive())


if __name__=="__main__":
    hero = Hero("GRace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

if __name__=='__main__':
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    print(hero.abilities)

if __name__=="__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero ("Dumbledore")

hero1.fight(hero2)

