
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        name_weapon = input("What is your weapon's name?")
        weapon_details = input("what exactly does your weapon do?")
        return Weapon(name_weapon, weapon_details)

    def create_armor(self):
        armor_name = input("What armor ar eyou using?")
        armor_details = input("What does your armor use?")
        return Armor(armor_name, armor_details)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # HINT: First create the ability, then add it to the hero
                ability = self.create_ability()
                hero.create_ability()

            elif add_item == "2":
                # HINT: First create the weapon, then add it to the hero
                weapon = self.create_weapon()
                hero.create_weapon()
            elif add_item == "3":
                # HINT: First create the armor, then add it to the hero
                armor = self.create_armor()
                hero.create_armor()
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    # HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers_2 = int(
            input("How many members would you like on Team Two? \n"))
        for i in range(numOfTeamMembers_2):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        team_one.attack(team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + \
              str(team_kills/team_deaths))

    # TODO: Now display the average K/D for Team Two
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + "average K/D was: " + \
              str(team_kills/team_deaths))
           # Major C.O.D. vibes

    # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

    # TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)


# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()
