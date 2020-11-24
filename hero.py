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
        # 0) Check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other
        # and each must take damage from the other's attack
        # 3) AFter each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName 
        # with the name of the hero, and end the fight loop
        while opponent.is_alive() is True and self.is_alive() is True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            #The above code takes care of 0, 1, and 2 conditions
        
            if opponent.is_alive() is False:
                print(f"{self.name} has won! ")
                return self.name
        
            if self.is_alive() is False:
                print(f"{opponent.name} has won! ")
                return opponent.name
            return
    

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)


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

