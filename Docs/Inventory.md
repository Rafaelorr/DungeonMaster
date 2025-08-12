# Inventory System Overview

**You don't need to rewrite the inventory system** to:

* Add new items
* Create new item categories
* Balance gameplay

Instead, modify the existing structure.

---

# Item Definitions

All items are defined in `ItemDatabase.py`, where you'll find:

* `item_database`: a nested dictionary of item categories and lists
* `randomItems`: miscellaneous items
* `consumables`: direct-use items like potions

Each item is an object of a class like:

* `Consumable`
* `Weapon`
* `Armor`

## To Add New Items:

1. Create a new instance of the item class.
2. Add it to the appropriate list in `item_database` or `randomItems`.

## To Add New Item Types:

1. Create a new class for the type (`Ring`, `Scroll`, etc.)
2. Update the `Inventory` methods (e.g., `use_item`, `equip_item`) to handle them.

---

# Character Interaction

The inventory system interacts with character objects in these ways:

* **Equipping items**: Items like weapons/armor check the character's `charClass` before equipping.
* **Using items**: Consumables apply their effects via `item.use(character)`.

## Your character class must support:

* `charClass`: string (e.g., "Mage", "Warrior")
* `equipItem(item)`: method for assigning gear

If you're modifying the character class, ensure compatibility with these expectations.

---

# Extending Game Mechanics

Here are some examples of game modifications and how they connect to the inventory system:

| You want to...                        | Do this                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| Add a new healing item                | Define it in `ItemDatabase` as a `Consumable`                                    |
| Create weapons exclusive to new class | Add `suitable_classes` to the item                                               |
| Track item durability                 | Extend `Weapon`/`Armor` with durability attributes and update `equip_item` logic |
| Add new item effects                  | Override `use()` in your `Consumable` subclass                                   |
| Log every inventory action            | Add logging inside `Inventory.add_item`, `use_item`, etc.                        |

---

# Dev Notes

* **Item names must be unique**. Inventory uses item names as keys.
* **No UI dependencies** exist here — this logic is purely backend.
* Adding **quest or story-critical items**? Treat them like regular items, but handle their use in quest logic.

---

# Before You Modify

* Check for existing helper functions before writing new logic.
* Keep gameplay logic (effects, requirements) in item or character classes — not the inventory.
* Use the existing item structure to avoid breaking compatibility with other systems.
