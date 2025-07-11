from Intro import intro_and_character_choice
from Inventory import Inventory
from EnchantedVillage import enchanted_village_adventure
from MysticalCaverns import mystical_caverns_adventure
from AncientRuins import ancient_ruins_adventure
from AbandonedCastle import abandoned_castle_adventure
from ForestOfShadows import forest_of_shadows_adventure
from DragonsLair import dragons_lair_adventure

def start_game():
    print("Welcome to Dragon's Demise Adventure Game!")
    player_character = intro_and_character_choice()

    if player_character is None:
        print("Game Over. Please restart to try again.")
        return

    player_inventory = Inventory()

    current_area = 'enchanted_village'
    game_over = False

    while not game_over:
        if current_area == 'enchanted_village':
            current_area = enchanted_village_adventure(player_character, player_inventory)
            print("\nYou venture forth to the Mystical Caverns.")

        elif current_area == 'mystical_caverns':
            current_area = mystical_caverns_adventure(player_character, player_inventory)
            print("\nYou discover the path to the Ancient Ruins.")

        elif current_area == 'ancient_ruins':
            current_area = ancient_ruins_adventure(player_character, player_inventory)
            print("\nYour journey leads you to the Abandoned Castle.")

        elif current_area == 'abandoned_castle':
            current_area = abandoned_castle_adventure(player_character, player_inventory)
            print("\nYou approach the mysterious Cavern of Echoes.")

        elif current_area == 'cavern_of_echoes':
            current_area = forest_of_shadows_adventure(player_character, player_inventory)
            print("\nFinally, you face the Dragon's Lair.")

        elif current_area == 'dragons_lair':
            dragons_lair_adventure(player_character, player_inventory)
            print("\nCongratulations! You have completed your adventure in Dragon's Demise.")
            game_over = True

        else:
            print("Unknown territory lies ahead.")
            game_over = True

if __name__ == "__main__":
    start_game()
