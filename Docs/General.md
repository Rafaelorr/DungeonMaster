#  Best Practices

Welcome ! If you're planning to **modify or maintain** the game, this document outlines best practices to help keep the project readable and fun to work on.

---

## General Principles

* **Read Before You Write**: Explore the existing structure (Inventory, ItemDatabase, Character) before adding new code.
* **Reuse Existing Systems**: Avoid duplicating functionality.
* **Keep Logic Modular**: Each system should have clear responsibilities.
* **Test Your Changes**: Add debug cases or run manual checks to confirm everything works as expected.

---

## Items & Inventory

* **Use Unique Item Names**: Item names are used as keys in the inventory. Conflicts = bugs.
* **Define Items in `ItemDatabase.py`**: This is the source of truth for all item types (weapons, armor, consumables, etc.).
* **Extend Item Classes**: Add functionality by subclassing (`Weapon`, `Armor`, etc.) rather than rewriting core logic.
* **Add `suitable_classes` to gear**: Ensure gear can only be equipped by appropriate character classes.
* **Document New Item Types**: If you create new item behavior (e.g. `Scroll`, `Ring`), update relevant docstrings or this README.

---

## Characters

* **Characters Must Support Required Interfaces**:

  * `charClass`: e.g., "Warrior", "Mage"
  * `equipItem(item)`: applies item effects/stats
* **Avoid Hardcoding Class Logic in Items**: Use `suitable_classes` or metadata.
* **Handle Invalid Equipment Gracefully**: Don't crash the game if someone tries to equip the wrong item.

---

## Inter-System Interaction

* **Let Items Handle Their Own Behavior**: For example, a consumable should define its own `.use(character)` logic.
* **Inventory Only Manages State**: Keep item effect logic inside item classes, not in `Inventory.py`.
* **Use Composition over Conditionals**: Avoid giant `if` chains.

---

## Code Style & Structure

* **Keep It Clean**: Follow consistent naming, spacing, and formatting.
* **Docstrings Matter**: Add docstrings to all public methods and classes.
* **Keep Classes Small & Focused**: Don’t overload one class with multiple responsibilities.

---

## Versioning & Changes

* **Test Before You Commit**: Don’t break main gameplay loops — test changes in isolation.
* **Use Meaningful Commits**: Write commit messages that clearly and short explain the changes

---

## Debugging Tips

* **Use `print()` for Debug Logs**: Especially in `add_item`, `equip_item`, etc., during development.
* **Add a Debug Mode Flag**: Toggle extra logging or cheats without modifying core logic.
* **Check for Typos in Item Names**: This is the most common source of "item not found" errors.

---

## Final Thoughts

* Keep things readable and understandable — your future self (or other people) will thank you.
* Ask before refactoring large systems — someone might already be working on it.

---

# Good to know

- The `gain_experience` function is currently a placeholder and needs implementation.
- Equipment is managed as simple item names; can be expanded into full item objects.
- The combat system currently uses random dice rolls for damage calculations.
- The code uses `exit()` on player death to end the game immediately.