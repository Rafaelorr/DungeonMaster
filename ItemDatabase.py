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

