#Main.py

from PlayerCharacter import Character, Database
from NewGameCharCreatorTransition import createCustomCharacter

def intro_and_character_choice():
    print("Welcome, adventurer, to a world of mystery, danger, and untold riches.")
    print("You are about to embark on a journey through treacherous swamps, haunted ruins, and mystical lands.")
    print("\nWho will you be in this epic tale?")
    print("1. Nameora Littleton - A half-elven messenger with a mysterious past.")
    print("2. Saad Amina - A work-for-hire herbalist with a knack for natural remedies.")
    print("3. Create your own character.")

    db = Database()  # Initialize the database

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return db.getCharacter("Nameora")
    elif choice == '2':
        return db.getCharacter("Saad Amina")
    elif choice == '3':
        return createCustomCharacter(db)
    else:
        print("Invalid choice. The adventure ends before it began.")
        return None

if __name__ == "__main__":
    player_character = intro_and_character_choice()
    if player_character:
        print(f"\nYou have chosen: {player_character.name}")
        # Here you can start the story portion or transition to another module/script
