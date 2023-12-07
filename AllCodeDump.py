#All Code Dump

#intro.py

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


######################################################

#DnDoneShot.py

from intro import intro_and_character_choice
from ItemDatabase import item_database  # Assuming this is where items are defined
from skills import *  # Import skill functions

def main_game_loop():
    print("Welcome to the Adventure!")

    player_character = intro_and_character_choice()
    if player_character is None:
        print("Game Over. Please restart to try again.")
        return

    # Game State Initialization
    current_location = "Starting Point"
    game_over = False

    # Main Game Loop
    while not game_over:
        print(f"\nYou are currently at: {current_location}")
        print("What would you like to do?")
        print("1. Explore")
        print("2. View Character")
        print("3. Use Item")
        print("4. Quit Game")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Exploration logic
            # Placeholder for exploration actions and encounters
            print("Exploring...")
            # ...

        elif choice == '2':
            # View Character Details
            print(f"\n{player_character}")
            # Additional character details can be shown here

        elif choice == '3':
            # Using an item
            # Placeholder for item usage logic
            print("Using item...")
            # ...

        elif choice == '4':
            print("Thank you for playing!")
            game_over = True
        else:
            print("Invalid choice. Please select a valid option.")

# Start the game
main_game_loop()



#############################################################

#NewGameCharCreatorTransition.py

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


#########################################################################

#PlayerCharacter.py

class Character:
    def __init__(self, name, race, charClass, level, abilities, equipment, background, maxHp, attack):
        self.name = name
        self.race = race
        self.charClass = charClass
        self.level = level
        self.abilities = abilities  # Abilities are stored here
        self.equipment = equipment
        self.background = background
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.attack = attack

    def levelUp(self):
        self.level += 1
        self.maxHp += 2
        self.attack += 2
        new_skill = self.unlockSkill()
        if new_skill:
            print(f"{self.name} has leveled up to level {self.level}! New skill unlocked: {new_skill}")
        else:
            print(f"{self.name} has leveled up to level {self.level}.")

    def unlockSkill(self):
        class_skills = {
            "Warrior": {1: "Charge", 2: "Defend", 3: "ShieldBash", 4: "Cleave", 5: "Fortify", 6: "Whirlwind", 7: "StoneSkin", 8: "BladeDance"},
            "Rogue": {1: "Stealth", 2: "Backstab", 3: "ShadowStrike", 4: "Ambush", 5: "Evasion", 6: "Assassinate", 7: "Vanish", 8: "Lacerate"},
            "Mage": {1: "Fireball", 2: "Teleport", 3: "ArcaneBlast", 4: "ElementalShield", 5: "ManaBurn", 6: "Blink", 7: "NetherPortal", 8: "Phase", 9: "SummonElemental", 10: "ThunderStrike"},
            "Paladin": {1: "Heal", 2: "Smite", 3: "HolyLight", 4: "DivineProtection", 5: "LayHands", 6: "Judgment", 7: "HolyNova", 8: "Consecrate", 9: "DivineFavor", 10: "GuardianAngel"},
            "Monk": {1: "Punch", 2: "Meditate", 3: "Flurry", 4: "Focus", 5: "Zen", 6: "TriplePunch", 7: "InnerPeace", 8: "RoundhouseKick", 9: "ZenMastery", 10: "FistOfTheHeavens"},
            "Cleric": {1: "Heal", 2: "Prayer", 3: "HolyLight", 4: "Bless", 5: "Resurrect", 6: "DivineFavor", 7: "Ward", 8: "DivineWrath", 9: "HolyNova"},
            "Bard": {1: "Sing", 2: "Inspire", 3: "Harmony", 4: "Dissonance", 5: "Ballad", 6: "Serenade", 7: "Requiem", 8: "Aria", 9: "Duet", 10: "EpicBallad"},
            "Ranger": {1: "BowShot", 2: "FindPath", 3: "Snipe", 4: "AnimalCompanion", 5: "QuickShot", 6: "Camouflage", 7: "Track", 8: "LongShot", 9: "AuraOfHealing", 10: "SummonFamiliar"}
        }

        skills = class_skills.get(self.charClass, {})
        new_skill = skills.get(self.level)
        if new_skill:
            self.abilities[new_skill] = True
            return new_skill
        return None

    def equipItem(self, item):
        if item in self.equipment:
            print(f"{self.name} is already equipped with {item}.")
        else:
            self.equipment.append(item)
            print(f"{self.name} has equipped {item}.")

    def takeDamage(self, damage):
        self.currentHp -= damage
        if self.currentHp <= 0:
            self.currentHp = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage, current HP: {self.currentHp}/{self.maxHp}")

    def setStartingEquipment(self, classEquipment):
        self.equipment = classEquipment.get(self.charClass, [])

    def copy(self):
        return Character(self.name, self.race, self.charClass, self.level, self.abilities.copy(), self.equipment.copy(), self.background, self.maxHp, self.attack)


class Database:
    def __init__(self):
        self.classEquipment = self.loadClassEquipment()
        self.originalCharacters = self.loadOriginalCharacters()
        self.currentCharacters = {name: char.copy() for name, char in self.originalCharacters.items()}

    def loadClassEquipment(self):
        return {
            "Mage": ["Staff", "Robe"],
            "Warrior": ["Sword", "Shield", "Chainmail Armor"],
            "Rogue": ["Daggers", "Leather Armor"],
            "Cleric": ["Mace", "Chainmail Armor"],
            "Paladin": ["Sword", "Shield", "Plate Armor"],
            "Ranger": ["Longbow", "Arrows", "Leather Armor"],
            "Bard": ["Lute", "Dagger", "Leather Armor"],
            "Monk": ["Quarterstaff", "Robe"]
        }

    def loadOriginalCharacters(self):
        characters = {
            "Nameora": Character("Nameora", "Elf", "Ranger", 2, {}, [], "Skilled messenger...", 20, 5),
            "Saad Amina": Character("Saad Amina", "Human", "Rogue", 2, {}, [], "Resourceful herbalist...", 18, 5)
        }
        for char in characters.values():
            char.setStartingEquipment(self.classEquipment)
        return characters

    def addCustomCharacter(self, name, race, charClass, level, abilities, background, maxHp, attack):
        customCharacter = Character(name, race, charClass, level, abilities, [], background, maxHp, attack)
        customCharacter.setStartingEquipment(self.classEquipment)
        self.originalCharacters[name] = customCharacter
        self.currentCharacters[name] = customCharacter.copy()

    def getCharacter(self, name):
        return self.currentCharacters.get(name)

    def resetToOriginal(self):
        self.currentCharacters = {name: char.copy() for name, char in self.originalCharacters.items()}

# Usage Example
db = Database()
db.addCustomCharacter("Custom Hero", "Human", "Paladin", 1, {}, "Valiant warrior...", 22, 5)

# Interact with a character
character = db.getCharacter("Custom Hero")
print(character.equipment)  # Outputs Paladin's starting gear



########################################################################################

#ClassDatabase.py

# Extending the game database to include more skills and spells for each class.
# Each class will have a list of skills and spells that unlock at each level up to level 10.

game_database_python_extended = {
    "classes": {
        "Warrior": {
            "base_hp": 30,
            "base_attack": 5,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Charge", "Defend"],
                "2": ["ShieldBash"],
                "3": ["Cleave"],
                "4": ["Fortify"],
                "5": ["Whirlwind"],
                "6": ["StoneSkin"],
                "7": ["BladeDance"]
            }
        },
        "Rogue": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["Stealth", "Backstab"],
                "2": ["ShadowStrike"],
                "3": ["Ambush"],
                "4": ["Evasion"],
                "5": ["Assassinate"],
                "6": ["Vanish"],
                "7": ["Lacerate"]
            }
        },
        "Mage": {
            "base_hp": 20,
            "base_attack": 7,
            "base_defense": 3,
            "level_up_skills": {
                "1": ["Fireball", "Teleport"],
                "2": ["ArcaneBlast"],
                "3": ["ElementalShield"],
                "4": ["ManaBurn"],
                "5": ["Blink"],
                "6": ["NetherPortal"],
                "7": ["Phase"],
                "8": ["SummonElemental"],
                "9": ["ThunderStrike"]
            }
        },
        "Paladin": {
            "base_hp": 35,
            "base_attack": 4,
            "base_defense": 6,
            "level_up_skills": {
                "1": ["Heal", "Smite"],
                "2": ["HolyLight"],
                "3": ["DivineProtection"],
                "4": ["LayHands"],
                "5": ["Judgment"],
                "6": ["HolyNova"],
                "7": ["Consecrate"],
                "8": ["DivineFavor"],
                "9": ["GuardianAngel"]
            }
        },
        "Monk": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Punch", "Meditate"],
                "2": ["Flurry"],
                "3": ["Focus"],
                "4": ["Zen"],
                "5": ["TriplePunch"],
                "6": ["InnerPeace"],
                "7": ["RoundhouseKick"],
                "8": ["ZenMastery"],
                "9": ["FistOfTheHeavens"]
            }
        },
        "Cleric": {
            "base_hp": 30,
            "base_attack": 4,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Heal", "Prayer"],
                "2": ["HolyLight"],
                "3": ["Bless"],
                "4": ["Resurrect"],
                "5": ["DivineFavor"],
                "6": ["Ward"],
                "7": ["DivineWrath"],
                "8": ["HolyNova"]
            }
        },
        "Bard": {
            "base_hp": 24,
            "base_attack": 5,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["Sing", "Inspire"],
                "2": ["Harmony"],
                "3": ["Dissonance"],
                "4": ["Ballad"],
                "5": ["Serenade"],
                "6": ["Requiem"],
                "7": ["Aria"],
                "8": ["Duet"],
                "9": ["EpicBallad"]
            }
        },
        "Ranger": {
            "base_hp": 28,
            "base_attack": 6,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["BowShot", "FindPath"],
                "2": ["Snipe"],
                "3": ["AnimalCompanion"],
                "4": ["QuickShot"],
                "5": ["Camouflage"],
                "6": ["Track"],
                "7": ["LongShot"],
                "8": ["AuraOfHealing"],
                "9": ["SummonFamiliar"]
            }
        }
    }
}


skill_descriptions = {
    # Warrior skills
    "Charge": "Rush towards an enemy, dealing extra damage on the next attack.",
    "Defend": "Increase your defense, reducing damage from the next attack against you.",
    "ShieldBash": "Use your shield to bash an enemy, causing a stun effect.",
    "Cleave": "Swing your weapon in a wide arc, hitting multiple enemies.",
    "Fortify": "Strengthen your armor, reducing incoming physical damage.",
    "Whirlwind": "Perform a spinning attack that hits multiple enemies around you.",
    "StoneSkin": "Transform your skin into stone, massively boosting your defense for a short time.",
    "BladeDance": "Engage in a deadly dance, striking all enemies around you multiple times.",
    # Rogue skills
    "Stealth": "Become invisible to enemies, making it easier to avoid combat or land the first strike.",
    "Backstab": "Perform a sneak attack that deals critical damage.",
    "ShadowStrike": "Strike from the shadows, dealing extra damage and applying a bleed effect.",
    "Ambush": "Set up an ambush, gaining the initiative in the next combat.",
    "Evasion": "Dodge the next attack against you, avoiding its damage.",
    "Assassinate": "Attempt to kill an enemy in one shot. Higher success rate on weaker enemies.",
    "Vanish": "Disappear from sight, avoiding all attacks for a short time.",
    "Lacerate": "Cause a deep wound on the enemy, causing them to bleed over time.",
    # Mage skills
    "Fireball": "Cast a fireball that deals AoE (Area of Effect) damage.",
    "Teleport": "Instantly move to a different location within a short distance.",
    "ArcaneBlast": "Release a burst of arcane energy, damaging enemies in a radius.",
    "ElementalShield": "Summon a shield of elemental energy, reducing incoming elemental damage.",
    "ManaBurn": "Burn an enemy's mana, dealing damage equal to the amount burned.",
    "Blink": "Teleport a short distance, even through walls.",
    "NetherPortal": "Open a portal to the nether realm, summoning demons to aid you.",
    "Phase": "Phase out of reality, avoiding all damage for a short time.",
    "SummonElemental": "Summon an elemental to fight for you.",
    "ThunderStrike": "Call down a bolt of lightning, dealing heavy damage to a single enemy.",
    # Paladin skills
    "Heal": "Restore a portion of HP to yourself or an ally.",
    "Smite": "Channel divine energy to deal extra damage on your next attack.",
    "HolyLight": "Summon a beam of holy light, healing allies and damaging undead enemies.",
    "DivineProtection": "Grant an ally a shield that absorbs a certain amount of damage.",
    "LayHands": "Lay your hands on an ally, fully restoring their HP.",
    "Judgment": "Pass divine judgment on an enemy, dealing heavy damage.",
    "HolyNova": "Emit a burst of holy light, healing allies and damaging enemies.",
    "Consecrate": "Consecrate the ground, causing damage to enemies who step on it.",
    "DivineFavor": "Gain the favor of the gods, increasing the effectiveness of your next spell.",
    "GuardianAngel": "Summon a guardian angel that protects an ally from the next fatal attack.",
    # Monk skills
    "Punch": "A quick and basic melee attack.",
    "Meditate": "Enter a state of deep focus, restoring some HP and Mana.",
    "Flurry": "Perform a series of quick punches, dealing damage to a single enemy.",
    "Focus": "Enter a focused state, increasing your next attack's damage.",
    "Zen": "Enter a Zen state, regaining full HP and Mana.",
    "TriplePunch": "Perform a triple punch combo, dealing heavy damage.",
    "InnerPeace": "Find inner peace, rapidly regenerating HP and Mana for a short time.",
    "RoundhouseKick": "Perform a roundhouse kick, hitting multiple enemies.",
    "ZenMastery": "Achieve the pinnacle of Zen mastery, making all your skills more potent.",
    "FistOfTheHeavens": "Summon a giant fist from the heavens to smash your enemies.",
    # Cleric Skills
    "Heal": "Restore a portion of HP to yourself or an ally.",
    "Prayer": "Say a prayer, granting a temporary buff to all party members.",
    "HolyLight": "Summon a beam of holy light, healing allies and damaging undead enemies.",
    "Bless": "Bless an ally, granting them a temporary boost to their abilities.",
    "Resurrect": "Bring an ally back to life with a portion of their HP.",
    "DivineFavor": "Gain the favor of the gods, increasing the effectiveness of your next spell.",
    "Ward": "Place a magical ward on an ally, granting resistance to magical attacks.",
    "DivineWrath": "Unleash the wrath of the gods, dealing massive damage to multiple enemies.",
    "HolyNova": "Emit a burst of holy light, healing allies and damaging enemies.",
    # Bard Skills
    "Sing": "Perform a song that grants temporary bonuses to your party.",
    "Inspire": "Motivate your allies, granting them a temporary boost in combat effectiveness.",
    "Harmony": "Play a harmonious tune, removing negative status effects from your party.",
    "Dissonance": "Play a dissonant tune, causing confusion among enemy ranks.",
    "Ballad": "Play a ballad that heals your party over time.",
    "Serenade": "Perform a serenade, charming an enemy to fight for you temporarily.",
    "Requiem": "Play a haunting melody, putting enemies to sleep.",
    "Aria": "Perform an aria that grants long-lasting buffs to your team.",
    "Duet": "Perform a duet with another Bard, combining the effects of both songs.",
    # Ranger Skills
    "BowShot": "Shoot an arrow from a distance, dealing damage to a single enemy.",
    "FindPath": "Discover hidden paths or shortcuts, reducing the time spent on travel.",
    "Snipe": "Take careful aim, dealing extra damage on your next bow shot.",
    "AnimalCompanion": "Summon an animal companion to assist you in combat.",
    "QuickShot": "Shoot an arrow quickly, reducing the time before your next action.",
    "Camouflage": "Blend into your surroundings, becoming nearly invisible.",
    "Track": "Track an enemy, revealing their location.",
    "LongShot": "Take a long-distance shot with your bow, dealing damage based on distance."
}


########################################################################

#ItemDatabase.py

class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

class Weapon(Item):
    def __init__(self, name, description, rarity, damage, suitable_classes):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.suitable_classes = suitable_classes

class Armor(Item):
    def __init__(self, name, description, rarity, defense, suitable_classes):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.suitable_classes = suitable_classes

# Rarity Scales
rarity_scales = {
    "Common": 1,
    "Uncommon": 1.25,
    "Rare": 1.5,
    "Epic": 2
}

# Defining the items for each class
# Reusing the warrior, mage, and ranger equipment from earlier
# ...

# Rogue Equipment
rogue_weapons = [
    Weapon("Dagger", "A sharp, lightweight dagger.", "Common", 7 * rarity_scales["Common"], ["Rogue"]),
    Weapon("Stiletto", "A thin, pointed dagger for precise strikes.", "Uncommon", 9 * rarity_scales["Uncommon"], ["Rogue"]),
    Weapon("Assassin's Blade", "A deadly weapon favored by stealthy assassins.", "Rare", 13 * rarity_scales["Rare"], ["Rogue"]),
    Weapon("Shadowfang", "A mystical blade that thrives in darkness.", "Epic", 17 * rarity_scales["Epic"], ["Rogue"])
]
rogue_armor = [
    Armor("Thief's Garb", "Lightweight attire for stealthy movement.", "Common", 4 * rarity_scales["Common"], ["Rogue"]),
    Armor("Shadow Cloak", "A cloak that aids in eluding detection.", "Uncommon", 6 * rarity_scales["Uncommon"], ["Rogue"]),
    Armor("Nimble Leather", "Armor that offers protection without sacrificing agility.", "Rare", 9 * rarity_scales["Rare"], ["Rogue"]),
    Armor("Ghost Armor", "Mythical armor that almost blends with the shadows.", "Epic", 13 * rarity_scales["Epic"], ["Rogue"])
]

# Paladin Equipment
paladin_weapons = [
    Weapon("Warhammer", "A sturdy warhammer.", "Common", 10 * rarity_scales["Common"], ["Paladin"]),
    Weapon("Greatsword", "A large sword that demands strength to wield.", "Uncommon", 12 * rarity_scales["Uncommon"], ["Paladin"]),
    Weapon("Divine Blade", "A sword infused with holy energy.", "Rare", 15 * rarity_scales["Rare"], ["Paladin"]),
    Weapon("Lightbringer", "A legendary sword radiating with divine light.", "Epic", 20 * rarity_scales["Epic"], ["Paladin"])
]
paladin_armor = [
    Armor("Chainmail", "Standard chainmail armor.", "Common", 6 * rarity_scales["Common"], ["Paladin"]),
    Armor("Plate Armor", "Heavy armor offering superior protection.", "Uncommon", 8 * rarity_scales["Uncommon"], ["Paladin"]),
    Armor("Holy Armor", "Sacred armor blessed by clerics.", "Rare", 11 * rarity_scales["Rare"], ["Paladin"]),
    Armor("Angel's Guard", "Celestial armor that exudes a holy aura.", "Epic", 16 * rarity_scales["Epic"], ["Paladin"])
]

# Monk Equipment
monk_weapons = [
    Weapon("Bo Staff", "A long wooden staff used in martial arts.", "Common", 6 * rarity_scales["Common"], ["Monk"]),
    Weapon("Nunchaku", "A traditional martial arts weapon.", "Uncommon", 8 * rarity_scales["Uncommon"], ["Monk"]),
    Weapon("Kusarigama", "A chain-sickle weapon with a versatile range.", "Rare", 12 * rarity_scales["Rare"], ["Monk"]),
    Weapon("Dragon Claws", "Fist weapons imbued with the spirit of a dragon.", "Epic", 18 * rarity_scales["Epic"], ["Monk"])
]
monk_armor = [
    Armor("Monk Robes", "Simple robes that allow for fluid movement.", "Common", 3 * rarity_scales["Common"], ["Monk"]),
    Armor("Silk Garb", "High-quality robes that provide slight protection.", "Uncommon", 5 * rarity_scales["Uncommon"], ["Monk"]),
    Armor("Harmony Vestments", "Robes that resonate with inner peace and strength.", "Rare", 8 * rarity_scales["Rare"], ["Monk"]),
    Armor("Celestial Robes", "Robes that seem to be woven from the fabric of the heavens.", "Epic", 12 * rarity_scales["Epic"], ["Monk"])
]

# Cleric Equipment
cleric_weapons = [
    Weapon("Mace", "A basic but effective bludgeoning weapon.", "Common", 8 * rarity_scales["Common"], ["Cleric"]),
    Weapon("Flail", "A weapon with a spiked ball attached by chain.", "Uncommon", 10 * rarity_scales["Uncommon"], ["Cleric"]),
    Weapon("Divine Scepter", "A ceremonial weapon that channels divine power.", "Rare", 14 * rarity_scales["Rare"], ["Cleric"]),
    Weapon("Hammer of Holiness", "A legendary hammer said to be blessed by the gods.", "Epic", 18 * rarity_scales["Epic"], ["Cleric"])
]
cleric_armor = [
    Armor("Priestly Vestments", "Robes signifying clerical devotion.", "Common", 4 * rarity_scales["Common"], ["Cleric"]),
    Armor("Blessed Chainmail", "Chainmail infused with holy energy.", "Uncommon", 6 * rarity_scales["Uncommon"], ["Cleric"]),
    Armor("Sacred Armor", "Armor that protects both body and spirit.", "Rare", 9 * rarity_scales["Rare"], ["Cleric"]),
    Armor("Divine Plate", "Plate armor said to be forged by celestial beings.", "Epic", 13 * rarity_scales["Epic"], ["Cleric"])
]

# Bard Equipment
bard_weapons = [
    Weapon("Rapier", "A light, sharp sword ideal for quick thrusts.", "Common", 7 * rarity_scales["Common"], ["Bard"]),
    Weapon("Lute Sword", "A cleverly disguised sword within a lute.", "Uncommon", 9 * rarity_scales["Uncommon"], ["Bard"]),
    Weapon("Bard's Blade", "A sword that resonates with musical harmony.", "Rare", 13 * rarity_scales["Rare"], ["Bard"]),
    Weapon("Song of Victory", "A mythical sword that is said to sing in battle.", "Epic", 17 * rarity_scales["Epic"], ["Bard"])
]
bard_armor = [
    Armor("Traveler's Clothes", "Comfortable clothing for a traveling bard.", "Common", 3 * rarity_scales["Common"], ["Bard"]),
    Armor("Performer's Garb", "Garb that is both protective and stylish.", "Uncommon", 5 * rarity_scales["Uncommon"], ["Bard"]),
    Armor("Minstrel's Mail", "A light armor that doesn't hinder performance.", "Rare", 8 * rarity_scales["Rare"], ["Bard"]),
    Armor("Maestro's Attire", "Elegantly crafted armor fit for a bardic legend.", "Epic", 12 * rarity_scales["Epic"], ["Bard"])
]

# Adding other classes if needed

# Item Database
item_database = {
    "Warrior": {
        "weapons": warrior_weapons,
        "armor": warrior_armor
    },
    "Mage": {
        "weapons": mage_weapons,
        "armor": mage_armor
    },
    "Ranger": {
        "weapons": ranger_weapons,
        "armor": ranger_armor
    },
    "Rogue": {
        "weapons": rogue_weapons,
        "armor": rogue_armor
    },
    "Paladin": {
        "weapons": paladin_weapons,
        "armor": paladin_armor
    },
    "Monk": {
        "weapons": monk_weapons,
        "armor": monk_armor
    },
    "Cleric": {
        "weapons": cleric_weapons,
        "armor": cleric_armor
    },
    "Bard": {
        "weapons": bard_weapons,
        "armor": bard_armor
    },
    # Add other classes
    # ...
}

# Example of accessing items
print(item_database["Cleric"]["weapons"][0].name)  # Outputs: Mace


class Consumable(Item):
    def __init__(self, name, description, rarity, effect):
        super().__init__(name, description, rarity)
        self.effect = effect

    def use(self, character):
        if "Health Potion" in self.name:
            heal_amount = 10 if "Greater" in self.name else 5
            healed_amount = min(heal_amount, character['max_hp'] - character['hp'])
            character['hp'] += healed_amount
            return f"{character['name']} restored {healed_amount} HP."

        if "Mana Potion" in self.name:
            mana_amount = 10 if "Greater" in self.name else 5
            restored_amount = min(mana_amount, character['max_mana'] - character['mana'])
            character['mana'] += restored_amount
            return f"{character['name']} restored {restored_amount} Mana."

# Consumables
consumables = [
    Consumable("Health Potion", "Restores 5 HP.", "Common", "Restore 5 HP"),
    Consumable("Greater Health Potion", "Restores 10 HP.", "Uncommon", "Restore 10 HP"),
    Consumable("Mana Potion", "Restores 5 Mana.", "Common", "Restore 5 Mana"),
    Consumable("Greater Mana Potion", "Restores 10 Mana.", "Uncommon", "Restore 10 Mana")
]


import random

class GenericItem(Item):
    def __init__(self, name, description, rarity, goldValue):
        super().__init__(name, description, rarity)
        self.goldValue = goldValue

    def __str__(self):
        return f"{self.name} (Worth: {self.goldValue} gold)"

# List of random items
randomItems = [
    GenericItem("Ancient Coin", "An old coin from a forgotten kingdom.", "Common", 5),
    GenericItem("Mysterious Gemstone", "A gemstone emitting a faint glow.", "Uncommon", 15),
    GenericItem("Old Scroll", "A scroll with indecipherable text.", "Common", 10),
    GenericItem("Enchanted Amulet", "An amulet with a mysterious aura.", "Rare", 30),
    GenericItem("Dragon's Tooth", "A tooth supposedly from a dragon.", "Epic", 50),
    GenericItem("Silver Ring", "A simple but elegant silver ring.", "Uncommon", 20),
    GenericItem("Herbal Potion", "A potion made from rare herbs.", "Common", 8),
    GenericItem("Crystal Vial", "A vial made from pure crystal.", "Rare", 25),
    GenericItem("Ancient Manuscript", "A manuscript containing ancient knowledge.", "Epic", 60),
    GenericItem("Magic Stone", "A small stone imbued with magic.", "Common", 12)
]

# Function to generate a random item
def generateRandomItem():
    return random.choice(randomItems)

# Example usage
randomItem = generateRandomItem()
print(f"You found: {randomItem}")



################################################################

#skills.py

# Warrior Skills

def charge(player, enemy):
    damage = player['attack'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Charge! {enemy['name']} took {damage} damage!"

def defend(player):
    player['defense'] *= 1.5
    return f"{player['name']} used Defend! Defense increased!"

def shieldBash(player, enemy):
    enemy['stunned'] = True
    return f"{player['name']} used Shield Bash! {enemy['name']} is stunned!"

def cleave(player, enemies):
    damage = player['attack']
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Cleave! All enemies took {damage} damage!"

def fortify(player):
    player['defense'] += 5
    return f"{player['name']} used Fortify! Defense increased by 5!"

def whirlwind(player, enemies):
    damage = player['attack'] * 0.8
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Whirlwind! All enemies took {damage} damage!"

def stoneSkin(player):
    player['defense'] *= 2
    return f"{player['name']} used Stone Skin! Defense greatly increased!"

def bladeDance(player, enemies):
    damage = player['attack'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Blade Dance! All enemies took {damage} damage!"


# Rogue Skills

def stealth(player):
    player['stealthed'] = True
    return f"{player['name']} used Stealth! Became invisible!"

def backstab(player, enemy):
    if player.get('stealthed', False):
        damage = player['attack'] * 3
        enemy['hp'] -= damage
        return f"{player['name']} used Backstab! {enemy['name']} took {damage} damage!"
    else:
        return f"{player['name']} tried to use Backstab but wasn't stealthed!"

def shadowStrike(player, enemy):
    damage = player['attack'] * 1.5
    enemy['hp'] -= damage
    enemy['bleeding'] = True
    return f"{player['name']} used Shadow Strike! {enemy['name']} took {damage} damage and is bleeding!"

def ambush(player, enemies):
    for enemy in enemies:
        enemy['surprised'] = True
    return f"{player['name']} used Ambush! Enemies are surprised!"

def evasion(player):
    player['evasion'] = True
    return f"{player['name']} used Evasion! Ready to dodge the next attack!"

def assassinate(player, enemy):
    if enemy['hp'] < player['attack'] * 2:
        enemy['hp'] = 0
        return f"{player['name']} used Assassinate! {enemy['name']} was instantly killed!"
    else:
        return f"{player['name']} attempted Assassinate on {enemy['name']}, but it failed!"

def vanish(player):
    player['stealthed'] = True
    player['evasion'] = True
    return f"{player['name']} used Vanish! Became invisible and evasive!"

def lacerate(player, enemy):
    damage = player['attack']
    enemy['hp'] -= damage
    enemy['bleeding'] = True
    return f"{player['name']} used Lacerate! {enemy['name']} took {damage} damage and is bleeding!"


# Mage Skills

def fireball(player, enemies):
    damage = player['magic'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Fireball! All enemies took {damage} damage!"

def teleport(player, location):
    player['location'] = location
    return f"{player['name']} used Teleport! Moved to {location}!"

def arcaneBlast(player, enemies):
    damage = player['magic_attack'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Arcane Blast! All enemies took {damage} damage!"

def elementalShield(player):
    player['elemental_resistance'] += 20
    return f"{player['name']} used Elemental Shield! Elemental resistance increased!"

def manaBurn(player, enemy):
    mana_damage = min(enemy['mana'], player['magic'])
    enemy['mana'] -= mana_damage
    enemy['hp'] -= mana_damage
    return f"{player['name']} used Mana Burn! {enemy['name']} lost {mana_damage} mana and HP!"

def blink(player, location):
    player['location'] = location
    return f"{player['name']} used Blink! Teleported to {location}!"

def nether_portal(player, enemies):
    for enemy in enemies:
        enemy['teleported'] = True
    return f"{player['name']} used Nether Portal! Enemies were teleported away!"

def phase(player):
    player['phased'] = True
    return f"{player['name']} used Phase! Became intangible!"

def summonElemental(player):
    player['elemental_summoned'] = True
    return f"{player['name']} summoned an Elemental! Elemental aid is at hand!"

def thunderStrike(player, enemy):
    damage = player['magic'] * 1.5
    enemy['hp'] -= damage
    enemy['stunned'] = True
    return f"{player['name']} used Thunder Strike! {enemy['name']} took {damage} damage and is stunned!"


# Paladin Skills

def heal(player):
    healing = player['magic']
    player['hp'] += healing
    return f"{player['name']} used Heal! Restored {healing} HP!"

def smite(player, enemy):
    damage = player['magic'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Smite! {enemy['name']} took {damage} damage!"

def holyLight(player, enemies):
    healing = player['magic']
    damage = player['magic'] * 0.8
    player['hp'] += healing
    for enemy in enemies:
        if enemy['type'] == 'undead':
            enemy['hp'] -= damage * 2
        else:
            enemy['hp'] -= damage
    return f"{player['name']} used Holy Light! Healed {healing} HP and damaged enemies!"

def divineProtection(player, ally):
    ally['defense'] += player['magic']
    return f"{player['name']} used Divine Protection! {ally['name']}'s defense increased!"

def layHands(player, ally):
    ally['hp'] = ally['max_hp']
    return f"{player['name']} used Lay Hands! {ally['name']} fully healed!"

def judgment(player, enemy):
    damage = player['magic'] * 2
    enemy['hp'] -= damage
    return f"{player['name']} used Judgment! {enemy['name']} took {damage} damage!"

def holyNova(player, allies, enemies):
    healing = player['magic']
    damage = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Holy Nova! Healed allies and damaged enemies!"

def consecrate(player, location):
    # Assuming this creates a zone with ongoing effect
    return f"{player['name']} used Consecrate! The ground at {location} is now consecrated!"

def divineFavor(player):
    player['attack'] *= 1.5
    player['defense'] *= 1.5
    return f"{player['name']} used Divine Favor! Attack and defense significantly increased!"

def guardianAngel(player, ally):
    ally['protected_by_angel'] = True
    return f"{player['name']} used Guardian Angel! {ally['name']} is now protected!"


# Monk Skills

def punch(player, enemy):
    damage = player['attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Punch! {enemy['name']} took {damage} damage!"

def meditate(player):
    player['hp'] += 10
    player['mana'] += 10
    return f"{player['name']} used Meditate! Restored 10 HP and 10 Mana!"

def flurry(player, enemy):
    damage = player['attack'] * 0.8
    for _ in range(3):
        enemy['hp'] -= damage
    return f"{player['name']} used Flurry! {enemy['name']} took {damage * 3} damage!"

def focus(player):
    player['attack'] *= 1.5
    return f"{player['name']} used Focus! Attack significantly increased!"

def zen(player):
    player['hp'] = player['max_hp']
    player['mana'] = player['max_mana']
    return f"{player['name']} used Zen! Fully restored HP and Mana!"

def triplePunch(player, enemy):
    damage = player['attack'] * 0.9
    for _ in range(3):
        enemy['hp'] -= damage
    return f"{player['name']} used Triple Punch! {enemy['name']} took {damage * 3} damage!"

def innerPeace(player):
    player['hp'] += player['max_hp'] * 0.5
    player['mana'] += player['max_mana'] * 0.5
    return f"{player['name']} used Inner Peace! Restored 50% of max HP and Mana!"

def roundhouseKick(player, enemies):
    damage = player['attack']
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Roundhouse Kick! All enemies took {damage} damage!"

def zenMastery(player):
    player['attack'] *= 1.5
    player['defense'] *= 1.5
    player['hp'] += player['max_hp'] * 0.2
    player['mana'] += player['max_mana'] * 0.2
    return f"{player['name']} used Zen Mastery! Increased attack, defense, and partially restored HP and Mana!"

def fistOfTheHeavens(player, enemy):
    damage = player['magic'] * 2
    enemy['hp'] -= damage
    return f"{player['name']} used Fist of the Heavens! {enemy['name']} took {damage} damage!"


# Cleric Skills

def heal(player, target):
    healing = player['magic'] * 1.2
    target['hp'] += healing
    return f"{player['name']} used Heal on {target['name']}! Restored {healing} HP!"

def prayer(player, allies):
    for ally in allies:
        ally['hp'] += player['magic'] * 0.5
    return f"{player['name']} used Prayer! Healed all allies!"

def holyLight(player, target):
    damage = player['magic'] * 1.5
    target['hp'] -= damage
    return f"{player['name']} used Holy Light on {target['name']}! {target['name']} took {damage} damage!"

def bless(player, target):
    target['attack'] *= 1.2
    target['defense'] *= 1.2
    return f"{player['name']} used Bless on {target['name']}! {target['name']}'s attack and defense increased!"

def resurrect(player, target):
    if target['hp'] <= 0:
        target['hp'] = player['magic'] * 2
        return f"{player['name']} used Resurrect on {target['name']}! {target['name']} has been brought back to life!"
    else:
        return f"{player['name']} tried to use Resurrect on {target['name']}, but it was unnecessary!"

def divineFavor(player):
    player['attack'] *= 1.3
    player['defense'] *= 1.3
    return f"{player['name']} used Divine Favor! Attack and defense increased!"

def ward(player, target):
    target['magic_resistance'] += 20
    return f"{player['name']} used Ward on {target['name']}! {target['name']}'s magic resistance increased!"

def divineWrath(player, enemies):
    damage = player['magic'] * 1.4
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Divine Wrath! All enemies took {damage} damage!"

def holyNova(player, allies, enemies):
    healing = player['magic'] * 0.8
    damage = player['magic'] * 0.6
    for ally in allies:
        ally['hp'] += healing
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Holy Nova! Healed allies and damaged enemies!"


# Bard Skills

def sing(player, allies):
    for ally in allies:
        ally['attack'] *= 1.1
        ally['defense'] *= 1.1
    return f"{player['name']} used Sing! All allies' attack and defense increased!"

def inspire(player, allies):
    for ally in allies:
        ally['attack'] *= 1.2
        ally['defense'] *= 1.2
    return f"{player['name']} used Inspire! All allies' attack and defense significantly increased!"

def harmony(player):
    player['status_cleared'] = True
    return f"{player['name']} used Harmony! Cleared negative status effects!"

def dissonance(player, enemies):
    for enemy in enemies:
        enemy['confused'] = True
    return f"{player['name']} used Dissonance! Enemies are confused!"

def ballad(player, allies):
    healing = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    return f"{player['name']} used Ballad! Healed all allies over time!"

def serenade(player, enemy):
    enemy['charmed'] = True
    return f"{player['name']} used Serenade on {enemy['name']}! {enemy['name']} is charmed!"

def requiem(player, enemies):
    for enemy in enemies:
        enemy['sleeping'] = True
    return f"{player['name']} used Requiem! Enemies put to sleep!"

def aria(player, allies):
    for ally in allies:
        ally['magic_resistance'] += 20
    return f"{player['name']} used Aria! All allies' magic resistance increased!"

def duet(player, anotherBard, allies):
    for ally in allies:
        ally['attack'] *= 1.3
        ally['defense'] *= 1.3
    return f"{player['name']} and {anotherBard['name']} performed a Duet! Significantly increased attack and defense for all allies!"

def epicBallad(player, allies):
    for ally in allies:
        ally['hp'] += player['magic'] * 1.5
        ally['mana'] += player['magic'] * 1.5
    return f"{player['name']} performed Epic Ballad! Massively restored HP and Mana for all allies!"


# Ranger Skills

def bowShot(player, enemy):
    damage = player['ranged_attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Bow Shot! {enemy['name']} took {damage} damage!"

def findPath(player):
    player['shortcuts_found'] += 1
    return f"{player['name']} used Find Path! Discovered a shortcut!"

def snipe(player, enemy):
    damage = player['ranged_attack'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Snipe! {enemy['name']} took {damage} damage!"

def animalCompanion(player):
    player['companion_summoned'] = True
    return f"{player['name']} summoned an Animal Companion! Companion aid is at hand!"

def quickShot(player, enemy):
    damage = player['ranged_attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Quick Shot! {enemy['name']} took {damage} damage!"

def camouflage(player):
    player['hidden'] = True
    return f"{player['name']} used Camouflage! Became nearly invisible!"

def track(player, enemy):
    enemy['tracked'] = True
    return f"{player['name']} used Track! {enemy['name']} is now being tracked!"

def longShot(player, enemy):
    distance = player['location'].distanceTo(enemy['location'])
    damage = player['ranged_attack'] * (1 + distance / 10)
    enemy['hp'] -= damage
    return f"{player['name']} used Long Shot! {enemy['name']} took {damage} damage from afar!"

def auraOfHealing(player, allies):
    healing = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    return f"{player['name']} activated Aura of Healing! Healed nearby allies!"

def summonFamiliar(player):
    player['familiar_summoned'] = True
    return f"{player['name']} summoned a Familiar! Familiar aid is at hand!"


# General Skills

def attack(player, enemy):
    weapon_dps = player['weapon']['dps']
    damage = player['attack'] * weapon_dps
    enemy['hp'] -= damage
    return f"{player['name']} attacks {enemy['name']} with {player['weapon']['name']} for {damage} damage!"

def dodge(player):
    roll = roll_d20() + player['agility_modifier']
    if roll >= 10:
        player['dodging'] = True
        return f"{player['name']} successfully dodged the next attack!"
    else:
        return f"{player['name']} failed to dodge!"

def rest(player):
    player['hp'] += 10  # Assuming fixed HP recovery
    player['mana'] += 10  # Assuming fixed Mana recovery
    return f"{player['name']} rests, regaining some health and mana."


def dodge(player):
    player['dodging'] = True
    return f"{player['name']} is prepared to dodge the next attack!"


def block(player):
    player['blocking'] = True
    return f"{player['name']} is prepared to block, ready to reduce the next incoming attack's damage by half!"
