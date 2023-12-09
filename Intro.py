# Intro.py

from CharacterDatabase import Database, Character

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

def allocate_skill_points(skill, skill_points):
    print(f"Allocate points for {skill} (Remaining points: {skill_points}): ")
    while True:
        try:
            points = int(input())
            if 0 <= points <= skill_points:
                return points  # Just return the allocated points
            else:
                print(f"Invalid input. Please allocate within your remaining skill points ({skill_points}).")
        except ValueError:
            print("Please enter a number.")

def determine_initial_attack(chosen_class):
    class_attack_values = {
        "Mage": 3,
        "Warrior": 5,
        "Rogue": 4,
        "Ranger": 3,
        "Paladin": 5,
        "Monk": 4,
        "Bard": 3,
        "Cleric": 2,
    }
    return class_attack_values.get(chosen_class, 4)  # Default value

def create_custom_character(database):
    print("\n--- Custom Character Creation ---")
    name = input("Enter your character's name: ")

    # Choosing a class
    classes_choices = list(database.classEquipment.keys())
    chosen_class = select_option(classes_choices, "Choose a Class:")

    # Choosing a race
    races_choices = ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]
    chosen_race = select_option(races_choices, "Choose a Race:")

    # Allocating skill points
    abilities = {}
    skill_points = 12
    skills = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for skill in skills:
        points = allocate_skill_points(skill, skill_points)
        abilities[skill] = points
        skill_points -= points

    # Creating the character
    attack_value = determine_initial_attack(chosen_class)
    custom_character = Character(name, chosen_race, chosen_class, 1, abilities, [], "Custom background", 20, attack_value)
    database.addCustomCharacter(name, chosen_race, chosen_class, 1, abilities, "Custom background", 20, attack_value)
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
