# Define skill points and choices for Classes and Races
initial_skill_points = 10
classes_choices = ["Mage", "Warrior", "Rogue", "Cleric", "Paladin", "Ranger", "Bard", "Monk"]
races_choices = ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]

# Helper function for selecting an option
def selectOption(options, prompt):
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

# Function to handle character creation for a custom character
def createCustomCharacter():
    print("\n--- Custom Character Creation ---")
    skillPoints = initial_skill_points
    skills = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}

    print(f"You have {skillPoints} skill points to allocate.")
    for skill in skills.keys():
        while True:
            try:
                points = int(input(f"Allocate points for {skill}: "))
                if 0 <= points <= skillPoints:
                    skills[skill] = points
                    skillPoints -= points
                    break
                else:
                    print("Invalid input. Please allocate within your remaining skill points.")
            except ValueError:
                print("Please enter a number.")

    chosenClass = selectOption(classes_choices, "Choose a Class:")
    chosenRace = selectOption(races_choices, "Choose a Race:")

    return {'Name': 'Custom', 'Class': chosenClass, 'Race': chosenRace, 'Skills': skills}

# Function to introduce the player to the game world and ask for character choice
def introAndCharacterChoice():
    print("Welcome, adventurer, to a world of mystery, danger, and untold riches.")
    # ... existing introduction text ...
    print("Who will you be in this epic tale?")
    print("1. Nameora Littleton - An elf with a mysterious past.")
    print("2. Saad Amina - A work-for-hire herbalist with a knack for natural remedies, now a Rogue.")
    print("3. Create your own character.")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return {'Name': 'Nameora', 'Class': 'Elf', 'Race': 'Ranger', 'Skills': {}}
    elif choice == '2':
        return {'Name': 'Saad Amina', 'Class': 'Human', 'Race': 'Rogue', 'Skills': {}}
    elif choice == '3':
        return createCustomCharacter()
    else:
        print("Invalid choice. The adventure ends before it began.")
        return None

# Main game loop
def mainGameLoop(playerCharacter):
    print(f"\nWelcome {playerCharacter['Name']} to the Adventure!")
    # The rest of your game loop here, using playerCharacter as the main character.

# Game initialization
characterChoice = introAndCharacterChoice()

if characterChoice:
    mainGameLoop(characterChoice)
else:
    print("Game over. Please restart to try again.")
