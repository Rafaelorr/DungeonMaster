# AncientRuins.py

from Combat import combat_round
from Inventory import Inventory
from skills import *
import random

def ancient_ruins_adventure(player_character, player_inventory):
    print("\nAfter your encounters in the Mystical Caverns, your journey leads you to the Ancient Ruins, an area filled with historical secrets and forgotten lore.")

    # Story point 1
    print("\nAs you enter, you notice intricate carvings on the ruin walls.")
    print("1. Examine the carvings closely")
    print("2. Proceed carefully without disturbing anything")
    choice = input("Your choice: ")
    if choice == '1':
        print("The carvings reveal the history of an ancient civilization and a hidden compartment opens up, revealing a magical scroll.")
        player_inventory.add_item('Ancient Scroll')
        print("Ancient Scroll added to your inventory.")
    else:
        print("You avoid the carvings, but stumble upon a hidden underground passage.")

    # Story point 2
    print("\nYou find a room with a mysterious, glowing orb.")
    print("1. Touch the orb")
    print("2. Observe from a distance")
    choice = input("Your choice: ")
    if choice == '1':
        print("The orb grants you a vision of the past, revealing the location of a secret chamber.")
    else:
        print("Observing from a distance, you notice a pattern on the floor leading to a hidden doorway.")

    # Story point 3 - Combat interaction
    print("\nGuardians of the ruins awaken to challenge your presence!")
    enemy = {"name": "Ancient Guardian", "hp": 25, "attack": 5, "defense": 4, "experience_value": 35}
    combat_round(player_character, enemy)
    print("After the battle, you find a rare artifact the guardians were protecting.")
    player_inventory.add_item('Rare Artifact')

    # Story point 4
    print("\nYou come across a grand hall with statues of ancient heroes.")
    print("1. Search the hall for clues")
    print("2. Pay respects and move on")
    choice = input("Your choice: ")
    if choice == '1':
        print("Your search reveals a hidden lever, opening a secret room filled with ancient weaponry.")
    else:
        print("You pay your respects. As you leave, a hidden compartment opens, revealing a hero's medallion.")
        player_inventory.add_item('Hero\'s Medallion')

    # Story point 5
    print("\nIn the deepest part of the ruins, you find a sealed tomb.")
    print("1. Attempt to open the tomb")
    print("2. Leave the tomb undisturbed")
    choice = input("Your choice: ")
    if choice == '1':
        print("The tomb opens, releasing an ancient spirit who grants you a powerful blessing.")
    else:
        print("You choose to leave the tomb undisturbed, respecting the rest of those long gone.")

    print("\nHaving explored the Ancient Ruins, you gather your findings and prepare for the next stage of your journey.")

    # Transition to next area
    next_area = 'dragons_lair'  # or any other area as per the storyline
    return next_area

# Example usage
# ancient_ruins_adventure(player_character, player_inventory)
