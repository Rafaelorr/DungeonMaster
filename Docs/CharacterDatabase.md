# `CharacterDatabase.py`

Manages characters and their data.

## Attributes
- `classEquipment` (dict): Equipment templates by class.
- `originalCharacters` (dict): Base character objects.
- `currentCharacters` (dict): Modifiable character copies for gameplay.

## Methods
- `loadClassEquipment()`: Returns equipment templates per class.
- `loadOriginalCharacters()`: Returns predefined base characters.
- `addCustomCharacter(...)`: Adds a user-defined character.
- `getCharacter(name)`: Retrieves a character by name.
- `resetToOriginal()`: Resets all current characters to originals.