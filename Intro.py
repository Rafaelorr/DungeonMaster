from CharacterDatabase import Database, Character

# Creating an instance of the character database
db = Database()

# Function to display a list of options and prompt the user to select one
def select_option(options, prompt):
    print("\n" + prompt)
    # Enumerate and display all available options
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
            # Ask user to allocate points for the current skill
            points = int(input())
            if 0 <= points <= skill_points:
                return points
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
    return class_attack_values.get(chosen_class, 4)

def create_custom_character(database):
    print("\n--- Custom Character Creation ---")
    name = input("Enter your character's name: ")

    classes_choices = list(database.classEquipment.keys())
    chosen_class = select_option(classes_choices, "Choose a Class:")

    races_choices = ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]
    chosen_race = select_option(races_choices, "Choose a Race:")

    abilities = {}
    skill_points = 12
    skills = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for skill in skills:
        points = allocate_skill_points(skill, skill_points)
        abilities[skill] = points
        skill_points -= points

    attack_value = determine_initial_attack(chosen_class)

    # Create the character object
    custom_character = Character(
        name,
        chosen_race,
        chosen_class,
        1,  # Starting level
        abilities,
        [],  # Empty inventory
        "Custom background",
        20,  # Starting health
        attack_value
    )

    # Add the character to the database
    database.addCustomCharacter(
        name,
        chosen_race,
        chosen_class,
        1,
        abilities,
        "Custom background",
        20,
        attack_value
    )

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
