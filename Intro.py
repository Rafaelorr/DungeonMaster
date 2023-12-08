# Merged intro.py

from CharacterDatabase import Database, Character

# Initialize the database
db = Database()

def select_option(options, prompt):
    print("\n" + prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            selection = int(input("Your choice: "))
            if 1 <= selection <= len(options):
                return options[selection - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a number.")

def create_custom_character(database):
    print("\n--- Custom Character Creation ---")
    name = input("Enter your character's name: ")

    print("\nChoose a Class:")
    classes_choices = list(database.classEquipment.keys())
    for i, class_choice in enumerate(classes_choices):
        print(f"{i + 1}. {class_choice}")
    chosen_class = select_option(classes_choices, "Choose a Class:")

    print("\nChoose a Race:")
    races_choices = ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]
    chosen_race = select_option(races_choices, "Choose a Race:")

    abilities = {}
    skill_points = 10
    print(f"\nYou have {skill_points} skill points to allocate.")
    skills = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for skill in skills:
        print(f"Allocate points for {skill} (Remaining points: {skill_points}): ")
        points = 0
        while True:
            try:
                points = int(input())
                if 0 <= points <= skill_points:
                    abilities[skill] = points
                    skill_points -= points
                    break
                else:
                    print(f"Invalid input. Please allocate within your remaining skill points ({skill_points}).")
            except ValueError:
                print("Please enter a number.")

    custom_character = Character(name, chosen_race, chosen_class, 1, abilities, [], "Custom background", 20)
    database.addCustomCharacter(name, chosen_race, chosen_class, 1, abilities, "Custom background", 20)
    return custom_character

def intro_and_character_choice():
    print("Welcome, adventurer, to a world of mystery, danger, and untold riches.")
    print("You are about to embark on a journey through treacherous swamps, haunted ruins, and mystical lands.")
    print("Your choices will determine your fate, and perhaps the fate of the world.")
    print("\nWho will you be in this epic tale?")
    print("1. Nameora Littleton - A half-elven messenger with a mysterious past.")
    print("2. Saad Amina - A work-for-hire herbalist with a knack for natural remedies.")
    print("3. Create your own character.")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return db.getCharacter("Nameora")
    elif choice == '2':
        return db.getCharacter("Saad Amina")
    elif choice == '3':
        return create_custom_character(db)
    else:
        print("Invalid choice. The adventure ends before it began.")
        return None

# If you have additional logic or functions from NewGameCharCreatorTransition.py that need to be included, add them below.
