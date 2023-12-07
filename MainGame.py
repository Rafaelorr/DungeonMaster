# Importing necessary modules
from Intro import intro_and_character_choice
from ForestOfShadows import forest_of_shadows_adventure
from MountainPass import mountain_pass_adventure
from DarkCaves import dark_caves_adventure
from AncientRuins import ancient_ruins_adventure
from DragonsLair import dragons_lair_adventure
from Inventory import Inventory  # Importing the Inventory class

# Function to start the game
def start_game():
    print("Welcome to Dragon's Demise Adventure Game!")
    player_character = intro_and_character_choice()

    if player_character is None:
        print("Game Over. Please restart to try again.")
        return

    # Initialize the player's inventory
    player_inventory = Inventory()

    # Add initial items to the inventory
    for item in player_character.equipment:
        player_inventory.add_item(item)

    # Main game loop
    current_area = 'forest_of_shadows'
    game_over = False

    while not game_over:
        # Display options for the player
        print("\nChoose an action:")
        print("1. Continue Adventure")
        print("2. View Character")
        print("3. View Inventory")
        print("4. Use Item")
        print("5. Equip Item")
        print("6. Quit Game")

        action = input("Your action: ")

        if action == '1':
            if current_area == 'forest_of_shadows':
                next_area = forest_of_shadows_adventure(player_character)
            elif current_area == 'mountain_pass':
                next_area = mountain_pass_adventure(player_character)
            elif current_area == 'dark_caves':
                next_area = dark_caves_adventure(player_character)
            elif current_area == 'ancient_ruins':
                next_area = ancient_ruins_adventure(player_character)
            elif current_area == 'dragons_lair':
                next_area = dragons_lair_adventure(player_character)
            # ... (handle other areas as needed)

            if next_area == 'end_game':
                print("Thank you for playing Dragon's Demise!")
                game_over = True
            else:
                current_area = next_area

        elif action == '2':
            print(player_character)  # Display character details

        elif action == '3':
            print(player_inventory)  # Display inventory contents

        elif action == '4':
            item_name = input("Enter the name of the item to use: ")
            print(player_inventory.use_item(item_name, player_character))

        elif action == '5':
            item_name = input("Enter the name of the item to equip: ")
            print(player_inventory.equip_item(item_name, player_character))

        elif action == '6':
            print("Thank you for playing Dragon's Demise!")
            game_over = True

        else:
            print("Invalid choice. Please select a valid option.")

# Starting the game
if __name__ == "__main__":
    start_game()
