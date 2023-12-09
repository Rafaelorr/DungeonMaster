from Combat import combat_round
from Inventory import Inventory
from skills import *
from ItemDatabase import consumables  # Import consumables
import random

def enchanted_village_adventure(player_character, player_inventory):
    print("You arrive at the Enchanted Village, shrouded in an eerie silence. The once vibrant streets are now desolate.")

    # Story point 1
    print("\nAs you walk through the village, you notice a strange glow coming from the old wizard's tower.")
    print("1. Investigate the tower")
    print("2. Continue exploring the village")
    choice = input("Your choice: ")
    if choice == '1':
        print("Inside the tower, you find a magical artifact and a note about a curse affecting the village.")
        # Assuming a similar approach for adding 'Magical Artifact'
        magical_artifact = next((item for item in consumables if item.name == "Magical Artifact"), None)
        if magical_artifact:
            player_inventory.add_item(magical_artifact)
            print("Magical Artifact added to your inventory.")
        else:
            print("No Magical Artifact found in the database.")
    else:
        print("Exploring the village, you stumble upon a hidden path leading to the outskirts.")

    # Story point 2
    print("\nYou encounter an injured villager, muttering about a dark presence in the forest.")
    print("1. Help the villager")
    print("2. Head towards the forest")
    choice = input("Your choice: ")
    if choice == '1':
        print("You use your skills to heal the villager, who thanks you and gives you a potion.")
        healing_potion = next((item for item in consumables if item.name == "Healing Potion"), None)
        if healing_potion:
            player_inventory.add_item(healing_potion)
            print("Healing Potion added to your inventory.")
        else:
            print("No Healing Potion found in the database.")
    else:
        print("Braving the dark forest, you find yourself surrounded by ominous shadows.")

    # Story point 3 - Combat interaction
    print("\nSuddenly, a group of shadowy creatures attacks!")
    enemy = {"name": "Shadow Creature", "hp": 15, "attack": 3, "defense": 2, "experience_value": 20}
    combat_round(player_character, enemy)
    print("After the battle, you find a mysterious rune on one of the defeated creatures.")
    # Assuming similar approach for adding 'Mysterious Rune'
    mysterious_rune = next((item for item in consumables if item.name == "Mysterious Rune"), None)
    if mysterious_rune:
        player_inventory.add_item(mysterious_rune)
        print("Mysterious Rune added to your inventory.")
    else:
        print("No Mysterious Rune found in the database.")

    # Story point 4
    print("\nYou discover a secret chamber underneath the village square.")
    print("1. Explore the chamber")
    print("2. Warn the villagers about the danger")
    choice = input("Your choice: ")
    if choice == '1':
        print("In the chamber, you find ancient scrolls detailing a forgotten ritual.")
        # Assuming similar approach for adding 'Ancient Scrolls'
        ancient_scrolls = next((item for item in consumables if item.name == "Ancient Scrolls"), None)
        if ancient_scrolls:
            player_inventory.add_item(ancient_scrolls)
            print("Ancient Scrolls added to your inventory.")
        else:
            print("No Ancient Scrolls found in the database.")
    else:
        print("You gather the villagers and form a plan to protect the village.")

    # Story point 5
    print("\nA powerful sorcerer, responsible for the curse, confronts you.")
    print("1. Engage in combat")
    print("2. Use the artifacts and scrolls to break the curse")
    choice = input("Your choice: ")
    if choice == '1':
        enemy = {"name": "Dark Sorcerer", "hp": 30, "attack": 5, "defense": 3, "experience_value": 50}
        combat_round(player_character, enemy)
        print("Defeating the sorcerer lifts the curse from the village.")
    else:
        print("Using the artifacts and scrolls, you perform a ritual that dissipates the dark energy.")

    print("\nThe village is saved, and you are hailed as a hero. It's time to continue your journey.")

    # Transition to next area
    next_area = 'mystical_caverns'  # or any other area as per the storyline
    return next_area

# Example usage
# enchanted_village_adventure(player_character, player_inventory)
