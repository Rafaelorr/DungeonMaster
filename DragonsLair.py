from Combat import combat_round
from skills import *

def dragons_lair_adventure(player_character, player_inventory):
    print("\nYou arrive at the foreboding entrance of the Dragon's Lair. A sense of dread and excitement fills the air.")

    # Story point 1
    print("\nAs you enter, you find the lair surprisingly illuminated with glowing crystals.")
    print("1. Collect some crystals")
    print("2. Proceed cautiously, ignoring the crystals")
    choice = input("Your choice: ")
    if choice == '1':
        print("You collect glowing crystals, which may have magical properties.")
        player_inventory.add_item('Glowing Crystals')
    else:
        print("You decide not to disturb the crystals and continue onward.")

    # Story point 2
    print("\nYou come across an injured adventurer who warns you about the dragon.")
    print("1. Help the adventurer")
    print("2. Ask for information about the dragon")
    choice = input("Your choice: ")
    adventurer_aid = False
    if choice == '1':
        print("After helping the adventurer, they share a secret passage that leads closer to the dragon.")
        adventurer_aid = True
    else:
        print("The adventurer shares valuable information about the dragon's weaknesses.")

    # Story point 3
    if not adventurer_aid:
        print("\nYou find a chamber filled with treasure.")
        print("1. Take some treasure")
        print("2. Leave the treasure undisturbed")
        choice = input("Your choice: ")
        if choice == '1':
            print("You collect some treasure, but it triggers a trap!")
            player_character.takeDamageByTraps(3,"a trap")
        else:
            print("You decide not to risk taking any treasure and proceed safely.")

    # Story point 4
    print("\nYou finally come face-to-face with the dragon.")
    print("1. Engage the dragon in battle")
    print("2. Attempt to communicate with the dragon")
    choice = input("Your choice: ")
    if choice == '1':
        print("You brace yourself for an epic battle with the dragon.")
        enemy = {"name": "Dragon", "hp": 100, "attack": 10, "defense": 8, "experience_value": 200}
        combat_round(player_character, enemy)
    else:
        print("You attempt to communicate with the dragon, discovering it is wise and ancient.")
        # Add logic for intel check UNFIN

    # Story point 5
    print("\nAfter your encounter with the dragon, you must decide your next move.")
    print("1. Leave the lair and continue your adventure")
    print("2. Stay in the lair to uncover more secrets")
    choice = input("Your choice: ")
    if choice == '1':
        print("You leave the lair, richer in wealth and experience, ready for your next adventure.")

    else:
        print("You choose to explore the lair further, uncovering hidden chambers and ancient lore.")

    print("\nThe Dragon's Lair adventure concludes.")

    next_area = 'game_end'
    return next_area
