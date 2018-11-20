"""
Oliver Chang
CSCI51p
11/16/2018
Assignmemt10
"""

from random import randint

class DnDCharacter:
    def __init__(self, name, chr_class="Fighter", race="Human"):
        self.name = name
        self.chr_class = chr_class
        self.race = race
        self.lvl = 1
        self.xp = 0
        self.hp = 8
        self. ability_scores = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0,
                                "Charisma": 0}
        self.ability_modifiers = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0,
                               "Charisma": 0}
        self.proficiency_bonus = 2
        self.hit_dice = "1d8"
        self.speed = 30

    def set_ability_scores(self):
        for i in self.ability_scores:
            dice_rolls = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
            dice_rolls.remove(min(dice_rolls))
            sum_rolls = 0
            for j in dice_rolls:
                sum_rolls += j
            self.ability_scores[i] = sum_rolls

    def set_ability_modifiers(self):
        for i in self.ability_scores:
            self.ability_modifiers[i] = int((self.ability_scores[i]-10)/2)

    def set_race_stats(self):
        if self.race == "Human":
            self.speed = 30

            for i in self.ability_scores:
                self.ability_scores[i] = self.ability_scores[i] + self.ability_modifiers[i]

        if self.race == "Elf":
            self.speed = 30
            self.ability_scores["Dexterity"] = self.ability_scores["Dexterity"] + 2

        if self.race == "Dwarf":
            self.speed = 25
            self.ability_scores["Constitution"] = self.ability_scores["Constitution"] + 2

    def set_class_stats(self):
        if self.chr_class == "Fighter":
            self.hit_dice = "1d10"
            self.hp = 8 + self.ability_modifiers["Constitution"]
        if self.chr_class == "Wizard":
            self.hit_dice = "1d6"
            self.hp = 8 + self.ability_modifiers["Constitution"]
        if self.chr_class == "Monk":
            self.hit_dice = "1d8"
            self.hp = 8 + self.ability_modifiers["Dexterity"]

    def get_ability_scores(self):
        return self.ability_scores

    def __str__(self):
        return "D&D Character stats:\n" + "Name: " + self.name + "\n" + "Class: " + self.chr_class + "\n" + "Race: " + \
               self.race + "\n" + "Hit Points: " + str(self.hp) + "\n" + "Experience:" + str(self.xp) + "\n" + \
               "Level: " + str(self.lvl) + "\n" + "Ability Scores: " + str(self.ability_scores) + "\n" +\
               "Ability Modifiers:" + str(self.ability_modifiers) + "\n"


def main():
    name1 = input("Welcome to D&D Character Creator! Please enter a name for the default character:\n")
    player1 = DnDCharacter(name1)
    player1.set_ability_scores()
    player1.set_ability_modifiers()
    player1.set_race_stats()
    player1.set_class_stats()

    name2 = input("Great! Now let's make a different companion. Type a name:\n")
    class2 = input("Type in one of the following classes: \n" + "Fighter\n" + "Wizard\n" + "Monk\n")
    race2 = input("Finally, type in one of the following races:\n" + "Human\n" + "Elf\n" + "Dwarf\n")

    player2 = DnDCharacter(name2, class2, race2)
    player2.set_ability_scores()
    player2.set_ability_modifiers()
    player2.set_race_stats()
    player2.set_class_stats()

    print("These are " + name1 + "'s stats")
    print(player1)
    print("These are " + name2 + "'s stats")
    print(player2)

    player1_ability_scores = player1.get_ability_scores()
    player2_ability_scores = player2.get_ability_scores()

    player1_count = 0
    player2_count = 0
    for i in player1_ability_scores:
        if player1_ability_scores[i] > player2_ability_scores[i]:
            player1_count += 1
        else:
            player2_count += 1

    if player1_count > player2_count:
        print("It looks like " + name1 + " has overall better stats than " + name2)
    elif player2_count > player1_count:
        print("It looks like " + name2 + " has overall better stats than " + name1)
    else:
        print("Both characters look equally balanced.")


if __name__ == "__main__":
    main()