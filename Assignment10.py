"""
Oliver Chang
CSCI51p
11/16/2018
Assignmemt10
"""

from random import randint

class DnDCharacter:
    def __init__(self, name, chr_class, race="Elf"):
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

    def set_race_stats(self):

        if self.race == "Human":
            self.speed = 30

            for i in self.ability_modifiers:
                self.ability_modifiers[i] = 1

            for i in self.ability_scores:
                self.ability_scores[i] = self.ability_scores[i] + self.ability_modifiers[i]

        if self.race == "Elf":
            self.speed = 30
            self.ability_modifiers["Dexterity"] = 2
            self.ability_scores["Dexterity"] = self.ability_scores["Dexterity"] + self.ability_modifiers["Dexterity"]

        if self.race == "Dwarf":
            self.speed = 25
            self.ability_modifiers["Constitution"] = 2
            self.ability_scores["Constitution"] = self.ability_scores["Constitution"] + self.ability_modifiers["Constitution"]

    def set_class_stats(self):
        if self.chr_class == "Fighter":
            self.hit_dice = "1d10"
            self.hp = randint(1, 10) + self.ability_modifiers["Constitution"]
        if self.chr_class == "Wizard":
            self.hit_dice = "1d6"
            self.hp = randint(1, 6) + self.ability_modifiers["Constitution"]

    def get_ability_scores(self):
        return self.ability_scores

    def __str__(self):
        return "D&D Character\n" + "Name: " + self.name + "\n" + "Class: " + self.chr_class + "\n" + "Race: " + \
               self.race + "\n" + "Ability Scores: " + str(self.ability_scores) + "\n"


def main():
    player1 = DnDCharacter("Plathorax", "Fighter", "Human")
    player1.set_ability_scores()
    player1.set_race_stats()
    player1.set_class_stats()

    print(player1)


if __name__ == "__main__":
    main()