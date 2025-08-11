# Modifying the Item & Equipment System

## Overview

This system includes:

* **Item class hierarchy**: Base `Item` class and specializations (`Weapon`, `Armor`, `Consumable`, etc.)
* **Item data per class**: Weapons and armor categorized by player class and rarity
* **Item creation system**: Auto-scales stats based on item rarity
* **Random items and consumables**: Includes non-equippable and usable items

---

## Class Architecture

### `Item` (Base Class)

```python
class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity
```

All item types inherit from `Item`. It stores:

* `name`: Item name
* `description`: Description
* `rarity`: Used for scaling or sorting items (`Common`, `Uncommon`, etc.)

---

### `Weapon` and `Armor` Classes

```python
class Weapon(Item):
    def __init__(...):
        ...
        self.damage = damage
        self.suitable_classes = suitable_classes
```

```python
class Armor(Item):
    def __init__(...):
        ...
        self.defense = defense
        self.suitable_classes = suitable_classes
```

* Add stats like `damage` or `defense`
* Define which classes can equip the item via `suitable_classes`

➡️ **Extend these classes** if you want attributes like:

* `attack_speed`, `critical_chance`, or `elemental_type`

---

### `Consumable` Class

```python
class Consumable(Item):
    def __init__(..., effect):
        ...
        self.effect = effect

    def use(self, character):
        ...
```

* Adds an `effect` and `use()` method
* Currently supports **HP and Mana potions**

➡️ You can override `use()` for more complex effects like:

* Temporary buffs
* Curing status effects
* Multi-character effects

---

### `GenericItem` Class

```python
class GenericItem(Item):
    def __init__(..., goldValue):
        ...
        self.goldValue = goldValue
```

* Used for collectibles, artifacts, and trade items
* Implements `__str__()` for formatted display

➡️ Useful for quests, shops, or lore-based exploration

---

## Rarity Scaling

```python
rarity_scales = {
    "Common": 1,
    "Uncommon": 1.25,
    "Rare": 1.5,
    "Epic": 2
}
```

Item stats like damage or defense scale based on this multiplier.

**Customizable** — Add new tiers like `"Legendary"` or `"Mythic"`.

---

## Item Factory Function

```python
def create_items(data, item_type):
    ...
```

* Takes raw stat data and builds full `Weapon` or `Armor` objects
* Scales base stats using rarity multiplier
* Assigns them to the current class

➡️ You can modify this to:

* Include random prefixes/suffixes (e.g., "Flaming Longsword")

---

## Equipment Data Structure

```python
class_equipment_data = {
    "Warrior": {
        "weapons": [...],
        "armor": [...]
    },
    ...
}
```

Each class has its own item list:

* Format: `(name, description, rarity, base_stat)`
* These lists get passed into `create_items()` to build the real item objects

Easily **expandable** — Add new classes or item entries directly here.

---

## Consumables List

```python
consumables = [
    Consumable("Health Potion", ..., "Restore 5 HP"),
    ...
]
```

* Stored as a simple list
* Can be randomized, dropped, or found

➡️ You can categorize them, e.g., `healing_items`, `mana_items`, `buffs`, etc.

---

## Random Item Pool

```python
randomItems = [
    GenericItem("Ancient Coin", ..., 5),
    ...
]
```

These are collectible or flavor items:

* No active effects
* May have trade value (`goldValue`)

➡️ Ideal for shops, loot drops or side quests.

---

## Example: Adding a New Weapon

1. Add to the weapon list in the appropriate class:

```python
("Thunderblade", "A sword that crackles with lightning.", "Epic", 25)
```

2. Done! It’ll be scaled and generated automatically.

---

## ✍️ Example: Creating a Custom Consumable

```python
class BuffPotion(Consumable):
    def use(self, character):
        character['attack'] += 5
        return f"{character['name']} feels empowered! Attack +5 for 3 turns."
```

---

## Suggested Modifications

| Feature               | How to Implement                                                      |
| --------------------- | --------------------------------------------------------------------- |
| **Shops**             | Filter `item_database` or `randomItems` by value or rarity            |
| **Loot drops**        | Randomly select from `randomItems` or `consumables` on monster defeat |
| **Item comparison**   | Compare new item stats to currently equipped gear                     |
| **JSON data loading** | Replace hardcoded data with external `.json` files                    |
| **Item durability**   | Add a `durability` attribute to weapons/armor                         |
| **Crafting system**   | Combine multiple `GenericItem`s into gear                             |

---

## Final Notes

This system is **designed for extensibility**:

* Easy to read and modify
* Supports class-specific gear and randomization
* Encourages object-oriented expansion