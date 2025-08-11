# Choose Your Own Adventure Game Code Documentation

## Files

---

### `PlayerCharacter.py`

Represents a player character with stats, abilities, equipment, and combat-related methods.

#### Attributes
- `name` (str): Character's name.
- `race` (str): Character's race.
- `charClass` (str): Character class (e.g., Warrior, Mage).
- `level` (int): Character's current level.
- `abilities` (dict): Ability scores and unlocked skills.
- `equipment` (list): Equipped items.
- `background` (str): Character's background story.
- `maxHp` (int): Maximum hit points.
- `currentHp` (int): Current hit points.
- `attack` (int): Attack stat.

#### Methods
- `levelUp()`: Increases level, boosts stats, and unlocks new skills.
- `unlockSkill()`: Unlocks new skills based on class and level.
- `skill_check(skill, dc)`: Performs a skill check (d20 + ability vs DC).
- `equipItem(item)`: Adds an item to equipment if not already equipped.
- `takeDamage(damage)`: Applies damage to the character, may cause a game over.
- `setStartingEquipment(classEquipment)`: Sets equipment based on class.
- `takeDamageByTraps(damage, source)`: Applies trap damage, may cause a game over.
- `copy()`: Returns a deep copy of the character instance.

---

### `CharacterDatabase.py`

Manages characters and their data.

#### Attributes
- `classEquipment` (dict): Equipment templates by class.
- `originalCharacters` (dict): Base character objects.
- `currentCharacters` (dict): Modifiable character copies for gameplay.

#### Methods
- `loadClassEquipment()`: Returns equipment templates per class.
- `loadOriginalCharacters()`: Returns predefined base characters.
- `addCustomCharacter(...)`: Adds a user-defined character.
- `getCharacter(name)`: Retrieves a character by name.
- `resetToOriginal()`: Resets all current characters to originals.

---

### `Combat.py`

#### `roll_dice(sides=6)`

Rolls a dice with specified number of sides (default 6).

- **Returns**: Integer result between 1 and `sides`.


#### `calculate_attack_damage(attack)`

Calculates attack damage by rolling a d6 plus attack stat.

- **Parameters**:
  - `attack` (int): Attack value.
- **Returns**: Damage dealt (minimum 0).

---

#### `gain_experience(player, experience)`

Placeholder function to add experience points and handle leveling.

- **Parameters**:
  - `player` (Character): Player gaining experience.
  - `experience` (int): XP gained.

---

#### `combat_round(player, enemy)`

Simulates one round of combat between player and enemy.

- **Parameters**:
  - `player` (Character): The player character.
  - `enemy` (dict): Enemy info with keys:
    - `'name'`: Enemy's name.
    - `'hp'`: Hit points.
    - `'attack'`: Attack value.
    - `'experience_value'`: XP awarded when defeated.

- **Effects**:
  - Reduces enemy and player HP by damage dealt.
  - Prints damage results.
  - Calls `gain_experience` on enemy defeat.
  - Ends game if player HP drops to 0 or below.

---

## Notes

- The `gain_experience` function is currently a placeholder and needs implementation.
- Equipment is managed as simple item names; can be expanded into full item objects.
- The combat system currently uses random dice rolls for damage calculations.
- The code uses `exit()` on player death to end the game immediately.

---
