# `PlayerCharacter.py`

Represents a player character with stats, abilities, equipment, and combat-related methods.

## Attributes
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

## Methods
- `levelUp()`: Increases level, boosts stats, and unlocks new skills.
- `unlockSkill()`: Unlocks new skills based on class and level.
- `skill_check(skill, dc)`: Performs a skill check (d20 + ability vs DC).
- `equipItem(item)`: Adds an item to equipment if not already equipped.
- `takeDamage(damage)`: Applies damage to the character, may cause a game over.
- `setStartingEquipment(classEquipment)`: Sets equipment based on class.
- `takeDamageByTraps(damage, source)`: Applies trap damage, may cause a game over.
- `copy()`: Returns a deep copy of the character instance.