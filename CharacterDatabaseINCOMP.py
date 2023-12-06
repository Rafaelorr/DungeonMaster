class Character:
    def __init__(self, name, race, charClass, level, abilities, equipment, background, maxHp):
        self.name = name
        self.race = race
        self.charClass = charClass
        self.level = level
        self.abilities = abilities
        self.equipment = equipment
        self.background = background
        self.maxHp = maxHp
        self.currentHp = maxHp

    def levelUp(self):
        self.level += 1
        # Add more functionality as needed for leveling up

    def addItem(self, item):
        self.equipment.append(item)

    def equipItem(self, item):
        if item not in self.equipment:
            print(f"{item} not in equipment.")
            return
        # Implement specific logic for equipping items

    def takeDamage(self, damage):
        self.currentHp -= damage
        if self.currentHp < 0:
            self.currentHp = 0
            print(f"{self.name} has been defeated!")

    def copy(self):
        return Character(self.name, self.race, self.charClass, self.level, self.abilities.copy(),
                         self.equipment.copy(), self.background, self.maxHp)

    def setStartingEquipment(self, classEquipment):
        self.equipment = classEquipment.get(self.charClass, [])

class Database:
    def __init__(self):
        self.classEquipment = self._loadClassEquipment()
        self.originalCharacters = self._loadOriginalCharacters()
        self.currentCharacters = {name: char.copy() for name, char in self.originalCharacters.items()}

    def _loadClassEquipment(self):
        return {
            "Mage": ["Staff", "Robe"],
            "Warrior": ["Sword", "Shield", "Chainmail Armor"],
            "Rogue": ["Daggers", "Leather Armor"],
            "Cleric": ["Mace", "Chainmail Armor"],
            "Paladin": ["Sword", "Shield", "Plate Armor"],
            "Ranger": ["Longbow", "Arrows", "Leather Armor"],
            "Bard": ["Lute", "Dagger", "Leather Armor"],
            "Monk": ["Quarterstaff", "Robe"],
            # Add other classes and their starting equipment here
        }

    def _loadOriginalCharacters(self):
        characters = {
            "Nameora": Character("Nameora", "Elf", "Ranger", 2, [], [], "Skilled messenger...", 20),
            "Saad Amina": Character("Saad Amina", "Human", "Rogue", 2, [], [], "Resourceful herbalist...", 18),
            # Add other predefined characters here
        }
        for char in characters.values():
            char.setStartingEquipment(self.classEquipment)
        return characters

    def addCustomCharacter(self, name, race, charClass, level, abilities, background, maxHp):
        customCharacter = Character(name, race, charClass, level, abilities, [], background, maxHp)
        customCharacter.setStartingEquipment(self.classEquipment)
        self.originalCharacters[name] = customCharacter
        self.currentCharacters[name] = customCharacter.copy()

    def getCharacter(self, name):
        return self.currentCharacters.get(name)

    def resetToOriginal(self):
        self.currentCharacters = {name: char.copy() for name, char in self.originalCharacters.items()}

# Usage Example
db = Database()
db.addCustomCharacter("Custom Hero", "Human", "Paladin", 1, [], "Valiant warrior...", 22)

# Interact with a character
character = db.getCharacter("Custom Hero")
print(character.equipment)  # Outputs Paladin's starting gear
