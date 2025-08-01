from Combat import combat_round
from skills import *

def mystical_caverns_adventure(player_character, player_inventory):
    print("Having saved the Enchanted Village, you now find yourself at the entrance of the Mystical Caverns, rumored to be filled with ancient magic and hidden dangers.")

    # Story point 1
    print("\nAs you venture deeper, you discover glowing runes on the cave walls.")
    print("1. Study the runes")
    print("2. Proceed cautiously without touching anything")
    choice = input("Your choice: ")
    if choice == '1':
        print("The runes reveal the location of a hidden chamber filled with treasure.")
        player_inventory.add_item('Ancient Coin')
        print("Ancient Gold Coin added to your inventory.")
    else:
        print("You avoid the runes and find a hidden path leading further into the cavern.")

    # Story point 2
    print("\nYou encounter a group of lost explorers.")
    print("1. Help them find a way out")
    print("2. Explore together")
    choice = input("Your choice: ")
    if choice == '1':
        print("You lead them to safety and they reward you with a mystical amulet.")
        player_inventory.add_item('Mystical Amulet')
        print("Mystical Amulet added to your inventory.")
    else:
        print("Exploring together, you come across a room filled with rare crystals.")

    # Story point 3 - Combat interaction
    print("\nA guardian creature attacks to protect the crystals!")
    enemy = {"name": "Cave Guardian", "hp": 20, "attack": 4, "defense": 3, "experience_value": 30}
    combat_round(player_character, enemy)
    print("After defeating the guardian, you collect some of the rare crystals.")
    player_inventory.add_item('Rare Crystals')

    # Story point 4
    print("\nYou find an ancient altar with a mysterious artifact.")
    print("1. Take the artifact")
    print("2. Leave it undisturbed")
    choice = input("Your choice: ")
    if choice == '1':
        print("The artifact grants you enhanced magical powers.")
        player_character.abilities["Constitution"] += 1
        player_character.abilities["Intelligence"] += 1
        player_character.abilities["Wisdom"] += 1
    else:
        print("You respect the sanctity of the altar and leave the artifact.")

    # Story point 5
    print("\nDeep in the caverns, you come across an underground lake.")
    print("1. Explore the lake")
    print("2. Continue through a narrow tunnel")
    choice = input("Your choice: ")
    if choice == '1':
        print("In the lake, you find a submerged passage leading to a hidden area.")
    else:
        print("The narrow tunnel leads to a chamber with historical inscriptions about the caverns.")

    print("\nHaving explored the Mystical Caverns, you prepare to journey to the next destination.")

    next_area = 'ancient_ruins'
    return next_area
