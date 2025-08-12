# Character Creation and Selection System

## File Dependencies

```python
from CharacterDatabase import Database, Character
```

This system depends on an external module:

* `Database`: Stores pre-made and custom characters.
* `Character`: Represents an individual character.

---

## Core Components

### 1. `db = Database()`

* Instantiates the main character database.
* Used for fetching predefined characters or adding new ones.

---

### 2. `select_option(options, prompt)`

```python
def select_option(options, prompt):
    ...
```

* Displays a numbered list of choices.
* Handles input and validation.
* Used to select class and race.

**You can use this** anywhere you need option selection.

---

### 3. `allocate_skill_points(skill, skill_points)`

```python
def allocate_skill_points(skill, skill_points):
    ...
```

* Prompts the player to assign points to a skill.
* Ensures total allocation does not exceed the available pool.

---

### 4. `determine_initial_attack(chosen_class)`

```python
def determine_initial_attack(chosen_class):
    ...
```

* Assigns a starting attack value based on class.
* Default fallback value: 4

Customize this dictionary to add new classes or rebalance stats.

---

## Character Creation Logic

### `create_custom_character(database)`

This is where players build their own character.

#### Steps:

1. **Name entry**
2. **Class selection**
3. **Race selection**

   * Hardcoded race options:

     ```python
     ["Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Dragonborn", "Tiefling"]
     ```
4. **Skill point allocation**

   * 12 points split across: `Strength`, `Dexterity`, `Constitution`, `Intelligence`, `Wisdom`, `Charisma`
5. **Calculate attack value**
6. **Create a `Character` object**
7. **Add to the database**

```python
custom_character = Character(...)
database.addCustomCharacter(...)
```

Developers can:

* Add **backgrounds** or **starting items** here
* Replace the hardcoded `20` health with something class-based

---

## Predefined Character Selection

```python
def intro_and_character_choice():
    ...
```

This function introduces the player and presents three choices:

1. Use predefined character `Nameora Littleton`
2. Use predefined character `Saad Amina`
3. Create a custom character

The selection returns a full `Character` object or `None` if input is invalid.

Add more predefined characters by modifying the `CharacterDatabase`.

---

## Example: Add a New Predefined Character

In `CharacterDatabase.py`, add:

```python
self.characters["Thorn Shadowstep"] = Character(
    "Thorn Shadowstep",
    "Half-Orc",
    "Rogue",
    1,
    {"Strength": 2, "Dexterity": 6, "Constitution": 2, "Intelligence": 0, "Wisdom": 1, "Charisma": 1},
    [],
    "Raised in the undercity of a fallen kingdom.",
    18,
    5
)
```

Then, update `intro_and_character_choice()`:

```python
print("4. Thorn Shadowstep - A rogue with a vengeful heart.")
...
elif choice == '4':
    return db.getCharacter("Thorn Shadowstep")
```

---

## Suggested Modifications

| Feature                            | How to Add                                                           |
| ---------------------------------- | -------------------------------------------------------------------- |
| Additional stats (e.g. Luck, Mana) | Extend the `Character` class                                         |
| Save/load characters               | Serialize and save custom characters                                 |
| Visual class/race descriptions     | Display lore or class benefits during selection                      |
| Random name generator              | Add name options for players who skip manual input                   |

---

## Developer Tips

* Use `select_option()` and `allocate_skill_points()` wherever you want to prompt for structured input.
* The separation between **predefined** and **custom characters** makes the system highly extensible.
* All changes to characters funnel through `Character` instances, keeping things consistent and testable.
