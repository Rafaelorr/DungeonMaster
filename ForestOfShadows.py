# ForestOfShadows.py

from Combat import combat_round
from Inventory import Inventory
from skills import *
import random

def forest_of_shadows_adventure(player_character, player_inventory):
    print("\nYour journey leads you to the mysterious Forest of Shadows, known for its magical aura and hidden dangers.")

    # Story point 1
    print("\nAs you traverse the forest, you hear a haunting melody.")
    print("1. Investigate the source of the melody")
    print("2. Continue on your path")
    choice = input("Your choice: ")
    if choice == '1':
        print("You find a bard trapped by magical vines. After helping them, they reward you with a magical lute.")
        player_inventory.add_item('Magical Lute')
    else:
        print("You avoid the melody and find a hidden path leading deeper into the forest.")

    # Story point 2
    print("\nYou come across an ancient tree with faces carved into its bark.")
    print("1. Touch the tree")
    print("2. Observe from a safe distance")
    choice = input("Your choice: ")
    if choice == '1':
        print("The tree awakens and shares ancient wisdom with you, enhancing your skills.")
        # Apply skill enhancement
    else:
        print("From a distance, you spot a hidden cache at the tree's base, containing a potion.")
        player_inventory.add_item('Elixir of Strength')

    # Story point 3 - Combat interaction
    print("\nShadow creatures emerge from the darkness to challenge you!")
    enemy = {"name": "Shadow Creature", "hp": 20, "attack": 4, "defense": 3, "experience_value": 30}
    combat_round(player_character, enemy)
    print("After defeating the creatures, you find a mysterious shadow gem.")
    player_inventory.add_item('Shadow Gem')

    # Story point 4
    print("\nYou stumble upon a hidden grove with a shimmering pond.")
    print("1. Drink from the pond")
    print("2. Collect some water and move on")
    choice = input("Your choice: ")
    if choice == '1':
        print("The water grants you a temporary boost in vitality.")
        # Apply temporary health boost
    else:
        print("You collect some water in a vial, which might be useful later.")
        player_inventory.add_item('Vial of Enchanted Water')

    # Story point 5
    print("\nDeep in the forest, you find a mysterious portal.")
    print("1. Step through the portal")
    print("2. Stay and explore more")
    choice = input("Your choice: ")
    if choice == '1':
        print("You step through the portal and find yourself in a different part of the forest.")
    else:
        print("You decide to stay and find a hidden chest containing gold.")
        player_inventory.add_item('Chest of Gold')

    print("\nHaving explored the Forest of Shadows, you gather your findings and prepare for the next stage of your journey.")

    # Transition to next area
    next_area = 'abandoned_castle'  # or any other area as per the storyline
    return next_area

# Example usage
# forest_of_shadows_adventure(player_character, player_inventory)
