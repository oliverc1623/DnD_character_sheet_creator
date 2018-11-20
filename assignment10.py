"""
Oliver Chang
CSCI51p
11/16/2018
Assignment 10
This program will define a class, D&D Character, and ask the user to create two characters
"""

from random import randint


class DnDCharacter:
    """
    Define the D&D Character Class
    """
    def __init__(self, name, chr_class="Fighter", race="Human"):
        """
        Initialize D&D character attributes
        :param name: str - name of character
        :param chr_class: str - type of character; optional, Fighter by default
        :param race: str - character' race; optional, Human by default
        """
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
        """
        Assign an int value to each key in the ability scores dictionary
        Each value is determined by generating 4 random numbers
        Then removing the smallest value and adding the rest
        :return: None
        """
        for i in self.ability_scores:
            # Make a list with 4 random ints from 1 to 6
            dice_rolls = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
            # Remove the smallest random int
            dice_rolls.remove(min(dice_rolls))
            sum_rolls = 0
            # Adding the sum of remaining generated numbers in list
            for j in dice_rolls:
                sum_rolls += j
            # Set the key a value in the dictoinary
            self.ability_scores[i] = sum_rolls

    def set_ability_modifiers(self):
        """
        Give each key in ability modifiers dictionary a value
        Value is calculated by subtracting 10 from each value in ability_scores and dividing 2
        :return: None
        """
        for i in self.ability_scores:
            self.ability_modifiers[i] = int((self.ability_scores[i]-10)/2)

    def set_race_stats(self):
        """
        Set the speed and adjust ability_scores based on the race selected
        :return: None
        """
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
        """
        Set the hit dice and hit point(hp) based on the class selected
        :return: None
        """
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
        """
        Returns the ability scores as a dictionary
        :return: dict - ability scores
        """
        return self.ability_scores

    def __str__(self):
        """
        Format class string to return every stat
        :return: str - character's info and stats
        """
        return "D&D Character stats:\n" + "Name: " + self.name + "\n" + "Class: " + self.chr_class + "\n" + "Race: " + \
               self.race + "\n" + "Hit Points: " + str(self.hp) + "\n" + "Hit Dice: " + self.hit_dice + "\n"\
               + "Speed: " + str(self.speed) + "\n" + "Experience:" + str(self.xp) + "\n" + \
               "Level: " + str(self.lvl) + "\n" + "Ability Scores: " + str(self.ability_scores) + "\n" +\
               "Ability Modifiers:" + str(self.ability_modifiers) + "\n"


def main():
    """
    Ask the user to create a default character(Fighter, Human) and a unique one
    Then compare the characters and tell the user which character has better stats
    :return: None
    """

    # Create Character 1
    name1 = input("Welcome to D&D Character Creator! Please enter a name for the default character:\n")
    player1 = DnDCharacter(name1)
    player1.set_ability_scores()
    player1.set_ability_modifiers()
    player1.set_race_stats()
    player1.set_class_stats()

    name2 = input("Great! Now let's make a different type of character. Type a name:\n")
    class2 = input("Type in one of the following classes: \n" + "Fighter\n" + "Wizard\n" + "Monk\n")
    race2 = input("Finally, type in one of the following races:\n" + "Human\n" + "Elf\n" + "Dwarf\n")

    # Create Character 2
    player2 = DnDCharacter(name2, class2, race2)
    player2.set_ability_scores()
    player2.set_ability_modifiers()
    player2.set_race_stats()
    player2.set_class_stats()

    print("These are " + name1 + "'s stats")
    print(player1)
    print("These are " + name2 + "'s stats")
    print(player2)

    # Get the ability scores for both characters
    player1_ability_scores = player1.get_ability_scores()
    player2_ability_scores = player2.get_ability_scores()

    # Initialize counters
    player1_count = 0
    player2_count = 0

    # Loop through keys in dictionary and check if one value is greater or less than the other
    for i in player1_ability_scores:
        if player1_ability_scores[i] > player2_ability_scores[i]:
            player1_count += 1
        else:
            player2_count += 1

    # Check the counters; player with greater number of count has better stats
    if player1_count > player2_count:
        print("It looks like " + name1 + " has overall better stats than " + name2)
    elif player2_count > player1_count:
        print("It looks like " + name2 + " has overall better stats than " + name1)
    else:
        print("Both characters look equally balanced.")


if __name__ == "__main__":
    main()
