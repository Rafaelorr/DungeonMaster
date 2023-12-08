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
# Warrior Equipment
warrior_weapons = [
    Weapon("Longsword", "A sturdy and reliable sword.", "Common", 10 * rarity_scales["Common"], ["Warrior"]),
    Weapon("Battle Axe", "A heavy axe capable of dealing massive damage.", "Uncommon", 12 * rarity_scales["Uncommon"], ["Warrior"]),
    Weapon("Warhammer", "A large hammer used for crushing blows.", "Rare", 15 * rarity_scales["Rare"], ["Warrior"]),
    Weapon("Excalibur", "The legendary sword of a once-great king.", "Epic", 20 * rarity_scales["Epic"], ["Warrior"])
]
warrior_armor = [
    Armor("Chainmail", "A suit of interlocking metal rings.", "Common", 5 * rarity_scales["Common"], ["Warrior"]),
    Armor("Plate Armor", "Heavy armor offering superior protection.", "Uncommon", 7 * rarity_scales["Uncommon"], ["Warrior"]),
    Armor("Dragon Scale Armor", "Armor forged from the scales of a dragon.", "Rare", 10 * rarity_scales["Rare"], ["Warrior"]),
    Armor("Armor of the Ancients", "Ancient armor said to be imbued with magical properties.", "Epic", 15 * rarity_scales["Epic"], ["Warrior"])
]

# Mage Equipment
mage_weapons = [
    Weapon("Staff of Illumination", "A staff that glows with an inner light.", "Common", 8 * rarity_scales["Common"], ["Mage"]),
    Weapon("Crystal Wand", "A wand made from pure crystal.", "Uncommon", 11 * rarity_scales["Uncommon"], ["Mage"]),
    Weapon("Orb of Power", "A mysterious orb that channels arcane energy.", "Rare", 14 * rarity_scales["Rare"], ["Mage"]),
    Weapon("Staff of the Archmage", "The staff once wielded by the legendary Archmage.", "Epic", 18 * rarity_scales["Epic"], ["Mage"])
]
mage_armor = [
    Armor("Robes of Insight", "Simple robes that enhance magical ability.", "Common", 3 * rarity_scales["Common"], ["Mage"]),
    Armor("Enchanted Cloak", "A cloak that protects against minor spells.", "Uncommon", 5 * rarity_scales["Uncommon"], ["Mage"]),
    Armor("Arcanist's Robe", "Robes that offer protection from magical attacks.", "Rare", 8 * rarity_scales["Rare"], ["Mage"]),
    Armor("Robes of the High Sorcerer", "Robes worn by the most powerful sorcerers.", "Epic", 12 * rarity_scales["Epic"], ["Mage"])
]

# Ranger Equipment
ranger_weapons = [
    Weapon("Short Bow", "A light, easy-to-use bow.", "Common", 9 * rarity_scales["Common"], ["Ranger"]),
    Weapon("Longbow", "A bow with great range and power.", "Uncommon", 11 * rarity_scales["Uncommon"], ["Ranger"]),
    Weapon("Crossbow", "A powerful bow that can pierce armor.", "Rare", 13 * rarity_scales["Rare"], ["Ranger"]),
    Weapon("Bow of the Forest Guardian", "A mystical bow said to be blessed by the forest spirits.", "Epic", 17 * rarity_scales["Epic"], ["Ranger"])
]
ranger_armor = [
    Armor("Leather Armor", "Flexible armor that does not hinder movement.", "Common", 4 * rarity_scales["Common"], ["Ranger"]),
    Armor("Camouflage Cloak", "A cloak that helps blend in with natural surroundings.", "Uncommon", 6 * rarity_scales["Uncommon"], ["Ranger"]),
    Armor("Elven Chainmail", "Lightweight chainmail made by elven smiths.", "Rare", 8 * rarity_scales["Rare"], ["Ranger"]),
    Armor("Armor of the Wild", "Magical armor that grants the wearer the agility of forest creatures.", "Epic", 11 * rarity_scales["Epic"], ["Ranger"])
]

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

