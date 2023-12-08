# Combat.py


import random

def roll_dice(sides=6):
    """Simulates rolling a dice with the given number of sides."""
    return random.randint(1, sides)

def calculate_attack_damage(attack, defense):
    """Calculates damage based on attack and defense, incorporating a dice roll."""
    damage = roll_dice() + attack - defense
    return max(damage, 0)  # Damage cannot be negative

def gain_experience(player, experience):
    """Add experience to the player and handle leveling up."""
    player['experience'] += experience
    if player['experience'] >= 100:  # Assuming 100 XP needed to level up
        player['level'] += 1
        player['experience'] -= 100
        player['attack'] += 2  # Increase attack and other stats as needed
        player['defense'] += 2
        print(f"{player['name']} has leveled up to level {player['level']}!")

def combat_round(player, enemy):
    """Handles a single round of combat."""
    player_damage = calculate_attack_damage(player['attack'], enemy['defense'])
    enemy_damage = calculate_attack_damage(enemy['attack'], player['defense'])

    enemy['hp'] -= player_damage
    player['hp'] -= enemy_damage

    print(f"{player['name']} deals {player_damage} damage to {enemy['name']}.")
    print(f"{enemy['name']} deals {enemy_damage} damage to {player['name']}.")

    if enemy['hp'] <= 0:
        print(f"{enemy['name']} has been defeated!")
        gain_experience(player, enemy['experience_value'])

    if player['hp'] <= 0:
        print(f"{player['name']} has been defeated! Loading from last save...")
        load_game()  # Implement the load_game function
