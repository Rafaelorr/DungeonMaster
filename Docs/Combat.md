# `Combat.py`

## `roll_dice(sides=6)`

Rolls a dice with specified number of sides (default 6).

- **Returns**: Integer result between 1 and `sides`.


## `calculate_attack_damage(attack)`

Calculates attack damage by rolling a d6 plus attack stat.

- **Parameters**:
  - `attack` (int): Attack value.
- **Returns**: Damage dealt (minimum 0).

---

## `gain_experience(player, experience)`

Placeholder function to add experience points and handle leveling.

- **Parameters**:
  - `player` (Character): Player gaining experience.
  - `experience` (int): XP gained.

---

## `combat_round(player, enemy)`

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