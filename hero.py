# Constructor
from random import choice 

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        players = [self, opponent]
        winner = (choice(players))

        print(f'{winner.name} won!')

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero ("Dumbledore")

hero1.fight(hero2)

