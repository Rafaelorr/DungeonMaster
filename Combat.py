#Combat.py

import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def calculate_attack_damage(attack):
    damage = roll_dice() + attack
    return max(damage, 0)  # Damage cannot be negative

def gain_experience(player, experience):
    #Implement XP system
    pass

def combat_round(player, enemy):
    player_damage = calculate_attack_damage(player.attack)
    enemy_damage = calculate_attack_damage(enemy['attack'])

    enemy['hp'] -= player_damage
    player.currentHp -= enemy_damage

    print(f"{player.name} deals {player_damage} damage to {enemy['name']}.")
    print(f"{enemy['name']} deals {enemy_damage} damage to {player.name}.")

    if enemy['hp'] <= 0:
        print(f"{enemy['name']} has been defeated!")
        gain_experience(player, enemy['experience_value'])

    if player.currentHp <= 0:
        print("Game Over.")
        #print(f"{player.name} has been defeated! Loading from last save...")
        # Implement the load game function

