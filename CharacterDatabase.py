# Represents a player character in the game
class Character:
    def __init__(self, name, race, charClass, level, abilities, equipment, background, maxHp, attack):
        self.name = name
        self.race = race
        self.charClass = charClass
        self.level = level
        self.abilities = abilities  # Dictionary of skills or powers
        self.equipment = equipment  # List of equipped items
        self.background = background
        self.maxHp = maxHp
        self.currentHp = maxHp  # starts full
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

    # Unlocks a new skill based on class and current level
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

        # Get the skills available for this character's class
        skills = class_skills.get(self.charClass, {})
        # Try to unlock a skill for the current level
        new_skill = skills.get(self.level)
        if new_skill:
            self.abilities[new_skill] = True  # Add to abilities
            return new_skill
        return None

    def equipItem(self, item):
        if item in self.equipment:
            print(f"{self.name} is already equipped with {item}.")
        else:
            self.equipment.append(item)
            print(f"{self.name} has equipped {item}.")

    # Applies damage to the character, and handles defeat if HP reaches zero
    def takeDamage(self, damage):
        self.currentHp -= damage
        if self.currentHp <= 0:
            self.currentHp = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage, current HP: {self.currentHp}/{self.maxHp}")

    # Sets the starting equipment based on the character’s class
    def setStartingEquipment(self, classEquipment):
        self.equipment = classEquipment.get(self.charClass, [])

    # Returns a deep copy of the character
    def copy(self):
        return Character(
            self.name,
            self.race,
            self.charClass,
            self.level,
            self.abilities.copy(),
            self.equipment.copy(),
            self.background,
            self.maxHp,
            self.attack
        )


# Manages characters
class Database:
    def __init__(self):
        # Loads class-based equipment templates
        self.classEquipment = self.loadClassEquipment()
        # Loads original predefined characters
        self.originalCharacters = self.loadOriginalCharacters()
        # Creates a modifiable copy of each character
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
        # Assign starting equipment to each character
        for char in characters.values():
            char.setStartingEquipment(self.classEquipment)
        return characters

    def addCustomCharacter(self, name, race, charClass, level, abilities, background, maxHp, attack):
        customCharacter = Character(name, race, charClass, level, abilities, [], background, maxHp, attack)
        customCharacter.setStartingEquipment(self.classEquipment)
        self.originalCharacters[name] = customCharacter
        self.currentCharacters[name] = customCharacter.copy()

    # Retrieves the current version of a character
    def getCharacter(self, name):
        return self.currentCharacters.get(name)

    # Resets all current characters to their original state
    def resetToOriginal(self):
        self.currentCharacters = {name: char.copy() for name, char in self.originalCharacters.items()}
