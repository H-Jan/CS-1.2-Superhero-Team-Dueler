
import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        ''' This method returns a random value between one half to the full attack
        power of the weapon '''
        #take in max damage and divide in half, using the two values as the range for
        # random function
        weapon_attack_damage = random.randint((self.max_damage // 2), self.max_damage)
        return weapon_attack_damage