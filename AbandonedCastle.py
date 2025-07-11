from Combat import combat_round
from skills import *

def abandoned_castle_adventure(player_character, player_inventory):
    print("\nYour adventure takes you to the Abandoned Castle, once a mighty fortress now left to ruins and shrouded in mystery.")

    # Story point 1
    print("\nIn the castle courtyard, you encounter a spectral knight.")
    print("1. Engage the knight")
    print("2. Try to communicate peacefully")
    choice = input("Your choice: ")
    if choice == '1':
        print("The knight attacks! Prepare for combat.")
        enemy = {"name": "Spectral Knight", "hp": 25, "attack": 6, "defense": 5, "experience_value": 40}
        combat_round(player_character, enemy)
    else:
        print("The knight shares the tale of the castle and bestows a blessing upon you.")
        # Add logic for a stat increase UNFIN

    # Story point 2
    print("\nYou find a grand library filled with ancient books.")
    print("1. Search the library for knowledge")
    print("2. Take some valuable books and proceed")
    choice = input("Your choice: ")
    if choice == '1':
        print("You gain insights into ancient magic and lore.")
        # Add logic for a stat increase
    else:
        print("You take some valuable books, which could be sold later.")
        player_inventory.add_item('Ancient Books')

    # Story point 3 - Puzzle interaction
    print("\nYou discover a room with a complex puzzle locking a chest.")
    # Add logic for puzzle mini-game UNFIN
    # if puzzle_solved:
    #     print("Inside the chest, you find a legendary weapon.")
    #     player_inventory.add_item('Legendary Weapon')
    # else:
    #     print("Unable to solve the puzzle, you leave the room.")

    # Story point 4
    print("\nIn the throne room, you encounter a ghostly figure on the throne.")
    print("1. Approach the figure")
    print("2. Search the room for clues")
    choice = input("Your choice: ")
    if choice == '1':
        print("The figure reveals itself as the former king and imparts wisdom.")
    else:
        print("You find a hidden compartment with a royal signet ring.")
        player_inventory.add_item('Royal Signet Ring')

    # Story point 5
    print("\nAtop the castle tower, you find a magical telescope.")
    print("1. Gaze into the telescope")
    print("2. Take the telescope with you")
    choice = input("Your choice: ")
    if choice == '1':
        print("You see visions of distant lands and gain foresight.")
    else:
        print("You take the telescope, which might reveal secrets later on.")
        player_inventory.add_item('Magical Telescope')

    print("\nHaving explored the Abandoned Castle, you gather your findings and prepare for the next stage of your journey.")

    next_area = 'dragons_lair'
    return next_area

