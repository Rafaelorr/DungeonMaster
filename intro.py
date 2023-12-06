from CharacterDatabaseINCOMP import Database, Character

# Initialize the database
db = Database()

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

def create_custom_character(database):
    print("\n--- Custom Character Creation ---")
    name = input("Enter your character's name: ")
    print("\nChoose a Class:")
    for i, class_choice in enumerate(database.classEquipment):
        print(f"{i + 1}. {class_choice}")
    chosen_class = ""
    while chosen_class not in database.classEquipment:
        class_selection = input("Your choice: ")
        chosen_class = database.classEquipment.get(class_selection, "")
    print("\nChoose a Race:")
    races_choices = ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]
    for i, race_choice in enumerate(races_choices):
        print(f"{i + 1}. {race_choice}")
    chosen_race = ""
    while chosen_race not in races_choices:
        race_selection = input("Your choice: ")
        try:
            chosen_race = races_choices[int(race_selection) - 1]
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid number.")
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

# Testing the function
chosen_character = intro_and_character_choice()
if chosen_character:
    print(f"You chose: {chosen_character.name}")
