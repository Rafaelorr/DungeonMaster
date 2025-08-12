# Skill Creation Guide

## Basic Skill Template

```python
def skill_name(player, [target(s)]):
    # Optional: Conditions or special checks
    # Calculate damage/effect
    # Apply changes to player or targets
    return f"{player['name']} used Skill Name! [Result text]"
```

---

## Skill Parameters

| Parameter  | Type     | Description                           |
| ---------- | -------- | ------------------------------------- |
| `player`   | `dict`   | The character using the skill         |
| `enemy`    | `dict`   | A single target enemy                 |
| `enemies`  | `list`   | List of enemies affected              |
| `ally`     | `dict`   | A single ally                         |
| `allies`   | `list`   | List of allies                        |

---

## Common Effects

| Effect Name   | How to Apply                          |
| ------------- | ------------------------------------- |
| Damage        | `enemy['hp'] -= damage`               |
| Heal          | `ally['hp'] += healing`               |
| Buff          | `player['attack'] *= 1.2`             |
| Debuff        | `enemy['defense'] *= 0.8`             |
| Status Effect | `enemy['stunned'] = True`             |
| Summon        | `player['companion_summoned'] = True` |
| Movement      | `player['location'] = location`       |
| Mana Cost     | `player['mana'] -= cost`              |

---

## Example 1: Basic Damage Skill

```python
def powerStrike(player, enemy):
    damage = player['attack'] * 2
    enemy['hp'] -= damage
    return f"{player['name']} used Power Strike! {enemy['name']} took {damage} damage!"
```

---

## Example 2: Area of Effect (AoE)

```python
def fireStorm(player, enemies):
    damage = player['magic'] * 1.3
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} cast Fire Storm! All enemies took {damage} damage!"
```

---

## Example 3: Buff + Heal

```python
def battleChant(player, allies):
    for ally in allies:
        ally['attack'] *= 1.2
        ally['hp'] += 10
    return f"{player['name']} used Battle Chant! Allies were healed and empowered!"
```

---

## Example 4: Conditional Skill

```python
def execution(player, enemy):
    if enemy['hp'] < player['attack'] * 2:
        enemy['hp'] = 0
        return f"{player['name']} used Execution! {enemy['name']} was slain instantly!"
    else:
        return f"{player['name']} tried Execution but {enemy['name']} was too strong!"
```

---

## Example 5: Apply Status Effects

```python
def poisonArrow(player, enemy):
    damage = player['ranged_attack'] * 0.8
    enemy['hp'] -= damage
    enemy['poisoned'] = True
    return f"{player['name']} shot a Poison Arrow! {enemy['name']} took {damage} damage and is poisoned!"
```

---

## Best Practices

* ✅ Use **clear, descriptive names** for functions and variables
* ✅ Always return a **battle log message**
* ✅ Include **status checks** where needed (e.g., is the target alive?)
* ✅ Use **consistent dictionary keys**
* ✅ Balance **damage/healing multipliers**
* ✅ Leave comments if effects are complex

---

## Skill Checklist

* [ ] Does it calculate damage or healing correctly?
* [ ] Does it modify stats or status properly?
* [ ] Does it return a clear message?
* [ ] Are edge cases handled (e.g. mana, hp limits)?
* [ ] Does it work on the intended targets (enemy, ally, all)?

---

##  Example Class Skill Block

```python
# Druid Skills

def entangle(player, enemy):
    enemy['rooted'] = True
    return f"{player['name']} used Entangle! {enemy['name']} is rooted!"

def barkskin(player):
    player['defense'] *= 1.5
    return f"{player['name']} used Barkskin! Defense increased!"

def natureWrath(player, enemies):
    damage = player['magic'] * 1.1
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Nature's Wrath! All enemies took {damage} damage!"
```

---