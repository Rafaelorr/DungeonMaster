import random

# ---------- Base Classes ----------

class Item:
    """Base class for all items."""
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

class Weapon(Item):
    """Weapon item with additional damage and class info."""
    def __init__(self, name, description, rarity, damage, suitable_classes):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.suitable_classes = suitable_classes

class Armor(Item):
    """Armor item with additional defense and class info."""
    def __init__(self, name, description, rarity, defense, suitable_classes):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.suitable_classes = suitable_classes

class Consumable(Item):
    """Consumable items with an effect and usage."""
    def __init__(self, name, description, rarity, effect):
        super().__init__(name, description, rarity)
        self.effect = effect

    def use(self, character):
        """Applies the consumable effect to a character."""
        if "Health Potion" in self.name:
            heal = 10 if "Greater" in self.name else 5
            healed = min(heal, character['max_hp'] - character['hp'])
            character['hp'] += healed
            return f"{character['name']} restored {healed} HP."

        elif "Mana Potion" in self.name:
            mana = 10 if "Greater" in self.name else 5
            restored = min(mana, character['max_mana'] - character['mana'])
            character['mana'] += restored
            return f"{character['name']} restored {restored} Mana."

class GenericItem(Item):
    """Random collectible or valuable item."""
    def __init__(self, name, description, rarity, goldValue):
        super().__init__(name, description, rarity)
        self.goldValue = goldValue

    def __str__(self):
        return f"{self.name} (Worth: {self.goldValue} gold)"

# ---------- Rarity Scaling ----------

rarity_scales = {
    "Common": 1,
    "Uncommon": 1.25,
    "Rare": 1.5,
    "Epic": 2
}

# ---------- Utility Functions ----------

def create_items(data, item_type):
    """Helper to create Weapon or Armor objects from data."""
    items = []
    for entry in data:
        name, desc, rarity, base_stat = entry
        scaled_stat = base_stat * rarity_scales[rarity]
        if item_type == "weapon":
            items.append(Weapon(name, desc, rarity, scaled_stat, [current_class]))
        else:
            items.append(Armor(name, desc, rarity, scaled_stat, [current_class]))
    return items

# ---------- Item Definitions Per Class ----------

# Format: (name, description, rarity, base_stat)
class_equipment_data = {
    "Warrior": {
        "weapons": [
            ("Longsword", "A sturdy and reliable sword.", "Common", 10),
            ("Battle Axe", "A heavy axe capable of dealing massive damage.", "Uncommon", 12),
            ("Warhammer", "A large hammer used for crushing blows.", "Rare", 15),
            ("Excalibur", "The legendary sword of a once-great king.", "Epic", 20)
        ],
        "armor": [
            ("Chainmail", "A suit of interlocking metal rings.", "Common", 5),
            ("Plate Armor", "Heavy armor offering superior protection.", "Uncommon", 7),
            ("Dragon Scale Armor", "Armor forged from the scales of a dragon.", "Rare", 10),
            ("Armor of the Ancients", "Ancient armor with magical properties.", "Epic", 15)
        ]
    },
    "Mage": {
        "weapons": [
            ("Staff of Illumination", "A staff that glows with an inner light.", "Common", 8),
            ("Crystal Wand", "A wand made from pure crystal.", "Uncommon", 11),
            ("Orb of Power", "A mysterious orb that channels arcane energy.", "Rare", 14),
            ("Staff of the Archmage", "The staff once wielded by the legendary Archmage.", "Epic", 18)
        ],
        "armor": [
            ("Robes of Insight", "Simple robes that enhance magical ability.", "Common", 3),
            ("Enchanted Cloak", "A cloak that protects against minor spells.", "Uncommon", 5),
            ("Arcanist's Robe", "Robes that offer protection from magical attacks.", "Rare", 8),
            ("Robes of the High Sorcerer", "Robes worn by the most powerful sorcerers.", "Epic", 12)
        ]
    },
    "Ranger": {
        "weapons": [
            ("Short Bow", "A light, easy-to-use bow.", "Common", 9),
            ("Longbow", "A bow with great range and power.", "Uncommon", 11),
            ("Crossbow", "A powerful bow that can pierce armor.", "Rare", 13),
            ("Bow of the Forest Guardian", "A mystical bow blessed by forest spirits.", "Epic", 17)
        ],
        "armor": [
            ("Leather Armor", "Flexible armor that does not hinder movement.", "Common", 4),
            ("Camouflage Cloak", "A cloak that helps blend in with surroundings.", "Uncommon", 6),
            ("Elven Chainmail", "Lightweight chainmail made by elven smiths.", "Rare", 8),
            ("Armor of the Wild", "Magical armor that grants agility of forest creatures.", "Epic", 11)
        ]
    },
    "Rogue": {
        "weapons": [
            ("Dagger", "A sharp, lightweight dagger.", "Common", 7),
            ("Stiletto", "A thin, pointed dagger for precise strikes.", "Uncommon", 9),
            ("Assassin's Blade", "A deadly weapon favored by stealthy assassins.", "Rare", 13),
            ("Shadowfang", "A mystical blade that thrives in darkness.", "Epic", 17)
        ],
        "armor": [
            ("Thief's Garb", "Lightweight attire for stealthy movement.", "Common", 4),
            ("Shadow Cloak", "A cloak that aids in eluding detection.", "Uncommon", 6),
            ("Nimble Leather", "Armor that offers protection without sacrificing agility.", "Rare", 9),
            ("Ghost Armor", "Mythical armor that blends with shadows.", "Epic", 13)
        ]
    },
    "Paladin": {
        "weapons": [
            ("Warhammer", "A sturdy warhammer.", "Common", 10),
            ("Greatsword", "A large sword that demands strength to wield.", "Uncommon", 12),
            ("Divine Blade", "A sword infused with holy energy.", "Rare", 15),
            ("Lightbringer", "A legendary sword radiating with divine light.", "Epic", 20)
        ],
        "armor": [
            ("Chainmail", "Standard chainmail armor.", "Common", 6),
            ("Plate Armor", "Heavy armor offering superior protection.", "Uncommon", 8),
            ("Holy Armor", "Sacred armor blessed by clerics.", "Rare", 11),
            ("Angel's Guard", "Celestial armor that exudes a holy aura.", "Epic", 16)
        ]
    },
    "Monk": {
        "weapons": [
            ("Bo Staff", "A long wooden staff used in martial arts.", "Common", 6),
            ("Nunchaku", "A traditional martial arts weapon.", "Uncommon", 8),
            ("Kusarigama", "A chain-sickle weapon with a versatile range.", "Rare", 12),
            ("Dragon Claws", "Fist weapons imbued with the spirit of a dragon.", "Epic", 18)
        ],
        "armor": [
            ("Monk Robes", "Simple robes that allow for fluid movement.", "Common", 3),
            ("Silk Garb", "High-quality robes that provide slight protection.", "Uncommon", 5),
            ("Harmony Vestments", "Robes resonating with inner peace and strength.", "Rare", 8),
            ("Celestial Robes", "Robes woven from the fabric of the heavens.", "Epic", 12)
        ]
    },
    "Cleric": {
        "weapons": [
            ("Mace", "A basic but effective bludgeoning weapon.", "Common", 8),
            ("Flail", "A weapon with a spiked ball attached by chain.", "Uncommon", 10),
            ("Divine Scepter", "A ceremonial weapon that channels divine power.", "Rare", 14),
            ("Hammer of Holiness", "A legendary hammer blessed by the gods.", "Epic", 18)
        ],
        "armor": [
            ("Priestly Vestments", "Robes signifying clerical devotion.", "Common", 4),
            ("Blessed Chainmail", "Chainmail infused with holy energy.", "Uncommon", 6),
            ("Sacred Armor", "Armor that protects both body and spirit.", "Rare", 9),
            ("Divine Plate", "Plate armor said to be forged by celestial beings.", "Epic", 13)
        ]
    },
    "Bard": {
        "weapons": [
            ("Rapier", "A light, sharp sword ideal for quick thrusts.", "Common", 7),
            ("Lute Sword", "A cleverly disguised sword within a lute.", "Uncommon", 9),
            ("Bard's Blade", "A sword that resonates with musical harmony.", "Rare", 13),
            ("Song of Victory", "A mythical sword that sings in battle.", "Epic", 17)
        ],
        "armor": [
            ("Traveler's Clothes", "Comfortable clothing for a traveling bard.", "Common", 3),
            ("Performer's Garb", "Garb that is both protective and stylish.", "Uncommon", 5),
            ("Minstrel's Mail", "A light armor that doesn't hinder performance.", "Rare", 8),
            ("Maestro's Attire", "Elegantly crafted armor fit for a bardic legend.", "Epic", 12)
        ]
    }
}


# ---------- Generate Item Database ----------

item_database = {}

for current_class, equipment in class_equipment_data.items():
    weapons = create_items(equipment["weapons"], "weapon")
    armor = create_items(equipment["armor"], "armor")
    item_database[current_class] = {"weapons": weapons, "armor": armor}

# ---------- Consumables ----------

consumables = [
    Consumable("Health Potion", "Restores 5 HP.", "Common", "Restore 5 HP"),
    Consumable("Greater Health Potion", "Restores 10 HP.", "Uncommon", "Restore 10 HP"),
    Consumable("Mana Potion", "Restores 5 Mana.", "Common", "Restore 5 Mana"),
    Consumable("Greater Mana Potion", "Restores 10 Mana.", "Uncommon", "Restore 10 Mana")
]

# ---------- Random Items ----------

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
    GenericItem("Magic Stone", "A small stone imbued with magic.", "Common", 12),
    GenericItem("Magical Artifact","A paper scroll imbued with magic.","Common",0),
    GenericItem("Mysterious Rune", "A Mysterious rune ","Common",0),
    GenericItem("Ancient Scrolls", "A collection of scrolls from the ancient past","Common",0)
]

def generateRandomItem():
    """Returns a random collectible item."""
    return random.choice(randomItems)