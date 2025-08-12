# Using *Dragon's Demise* as a Base for Your Own Text Adventure Game

This guide is for **devs** who want to modify or expand the *Dragon’s Demise* code to build their own custom text-based adventure games.

---

## Project Structure Overview

This project is modular. Each part of the game (intro, inventory, and adventure areas) is kept in separate files, which makes it **easy to customize** and **extend**.

### Key Components

| Module                                    | Purpose                                             |
| ----------------------------------------- | --------------------------------------------------- |
| `Intro.py`                                | Handles player introduction and character selection |
| `Inventory.py`                            | Defines the inventory system                        |
| `EnchantedVillage.py`, etc.               | Each contains a unique adventure area               |
| `main.py` (or the file with `start_game`) | Main game loop controller                           |

---

## How the Game is Structured

### `start_game()` Function

This is the **heart of the game**, and it manages:

1. Character creation
2. Inventory setup
3. Game loop and area progression
4. Ending the game

---

## How to Make It Your Own

### 1. **Customize the Story**

Each area (like `EnchantedVillage.py`) is a self-contained module with its own function (e.g., `enchanted_village_adventure`). Inside that function, you can:

* Add custom choices
* Branch the story
* Add dialogue and narration

**The function must return the name of the next area as a string.**

---

### 2. **Add New Areas**

Want to add a new level, like a “Haunted Forest”?

1. Create a new file: `HauntedForest.py`
2. Define a function in it:

   ```python
   def haunted_forest_adventure(player, inventory):
       # Your custom logic here
       return 'next_area_name'
   ```
3. Import it in your main script:

   ```python
   from HauntedForest import haunted_forest_adventure
   ```
4. Add it to the game loop:

   ```python
   elif current_area == 'haunted_forest':
       current_area = haunted_forest_adventure(player_character, player_inventory)
   ```

---

### 3. **Change the Inventory System**

The inventory is managed through the `Inventory` class. You can:

* Add new methods (e.g. `equip_weapon`, `check_weight_limit`)
* Store additional data (e.g. gold, quest items)
* Display inventory in new ways

---

### 4. **Create Branching Paths**

Right now, the game moves in a linear order:

```
Enchanted Village → Mystical Caverns → Ancient Ruins → Abandoned Castle → Dragon's Lair
```

To allow branching paths:

* Let adventure functions return **different next areas** based on player choices.
* Example:

  ```python
  choice = input("Do you go into the forest or the cave? ")
  if choice == 'forest':
      return 'haunted_forest'
  else:
      return 'icy_cave'
  ```

Then add those areas and functions just like any other.

---

### 5. **Replace Character Creation**

Modify `Intro.py` to:

* Let users choose classes, races, or skills
* Include backstory options
* Assign stats based on choices

---

## Example: Adding a New Area

### Step-by-Step

**1. Create the file:**
`MysticLake.py`

```python
def mystic_lake_adventure(player, inventory):
    print("You arrive at the mysterious Mystic Lake.")
    # Add logic here
    return 'dragons_lair'  # or any next area
```

**2. Import it:**

```python
from MysticLake import mystic_lake_adventure
```

**3. Add to the loop:**

```python
elif current_area == 'mystic_lake':
    current_area = mystic_lake_adventure(player_character, player_inventory)
```

**4. Branch to it from another area:**
In `ancient_ruins_adventure()`:

```python
choice = input("Enter the portal to the Mystic Lake? (yes/no): ")
if choice == 'yes':
    return 'mystic_lake'
```

---

## Best Practices

* **Keep functions short and focused** — one file per location.
* **Use clear return values** — each area should return a string indicating the next area.
* **Save and load** functionality can be added later using file I/O or JSON.
* **Use version control (like Git)** to track your changes and collaborate.

---

## Suggested Next Features

* Combat system
* Puzzle challenges
* Save/load progress
* Multiple endings
* Stat tracking and leveling up

---

## Final Notes

This game structure is perfect for:

* Beginner developers learning modular Python
* Writers wanting to build interactive fiction

With minimal Python knowledge, you can **swap out content**, **reorder the world**, and **craft a completely unique adventure**.

If you need help with creating a specific mechanic (e.g. combat, inventory UI, branching logic), just ask!