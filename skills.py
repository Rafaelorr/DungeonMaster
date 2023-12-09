#skills.py


# Warrior Skills

def charge(player, enemy):
    damage = player['attack'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Charge! {enemy['name']} took {damage} damage!"

def defend(player):
    player['defense'] *= 1.5
    return f"{player['name']} used Defend! Defense increased!"

def shieldBash(player, enemy):
    enemy['stunned'] = True
    return f"{player['name']} used Shield Bash! {enemy['name']} is stunned!"

def cleave(player, enemies):
    damage = player['attack']
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Cleave! All enemies took {damage} damage!"

def fortify(player):
    player['defense'] += 5
    return f"{player['name']} used Fortify! Defense increased by 5!"

def whirlwind(player, enemies):
    damage = player['attack'] * 0.8
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Whirlwind! All enemies took {damage} damage!"

def stoneSkin(player):
    player['defense'] *= 2
    return f"{player['name']} used Stone Skin! Defense greatly increased!"

def bladeDance(player, enemies):
    damage = player['attack'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Blade Dance! All enemies took {damage} damage!"


# Rogue Skills

def stealth(player):
    player['stealthed'] = True
    return f"{player['name']} used Stealth! Became invisible!"

def backstab(player, enemy):
    if player.get('stealthed', False):
        damage = player['attack'] * 3
        enemy['hp'] -= damage
        return f"{player['name']} used Backstab! {enemy['name']} took {damage} damage!"
    else:
        return f"{player['name']} tried to use Backstab but wasn't stealthed!"

def shadowStrike(player, enemy):
    damage = player['attack'] * 1.5
    enemy['hp'] -= damage
    enemy['bleeding'] = True
    return f"{player['name']} used Shadow Strike! {enemy['name']} took {damage} damage and is bleeding!"

def ambush(player, enemies):
    for enemy in enemies:
        enemy['surprised'] = True
    return f"{player['name']} used Ambush! Enemies are surprised!"

def evasion(player):
    player['evasion'] = True
    return f"{player['name']} used Evasion! Ready to dodge the next attack!"

def assassinate(player, enemy):
    if enemy['hp'] < player['attack'] * 2:
        enemy['hp'] = 0
        return f"{player['name']} used Assassinate! {enemy['name']} was instantly killed!"
    else:
        return f"{player['name']} attempted Assassinate on {enemy['name']}, but it failed!"

def vanish(player):
    player['stealthed'] = True
    player['evasion'] = True
    return f"{player['name']} used Vanish! Became invisible and evasive!"

def lacerate(player, enemy):
    damage = player['attack']
    enemy['hp'] -= damage
    enemy['bleeding'] = True
    return f"{player['name']} used Lacerate! {enemy['name']} took {damage} damage and is bleeding!"


# Mage Skills

def fireball(player, enemies):
    damage = player['magic'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Fireball! All enemies took {damage} damage!"

def teleport(player, location):
    player['location'] = location
    return f"{player['name']} used Teleport! Moved to {location}!"

def arcaneBlast(player, enemies):
    damage = player['magic_attack'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Arcane Blast! All enemies took {damage} damage!"

def elementalShield(player):
    player['elemental_resistance'] += 20
    return f"{player['name']} used Elemental Shield! Elemental resistance increased!"

def manaBurn(player, enemy):
    mana_damage = min(enemy['mana'], player['magic'])
    enemy['mana'] -= mana_damage
    enemy['hp'] -= mana_damage
    return f"{player['name']} used Mana Burn! {enemy['name']} lost {mana_damage} mana and HP!"

def blink(player, location):
    player['location'] = location
    return f"{player['name']} used Blink! Teleported to {location}!"

def nether_portal(player, enemies):
    for enemy in enemies:
        enemy['teleported'] = True
    return f"{player['name']} used Nether Portal! Enemies were teleported away!"

def phase(player):
    player['phased'] = True
    return f"{player['name']} used Phase! Became intangible!"

def summonElemental(player):
    player['elemental_summoned'] = True
    return f"{player['name']} summoned an Elemental! Elemental aid is at hand!"

def thunderStrike(player, enemy):
    damage = player['magic'] * 1.5
    enemy['hp'] -= damage
    enemy['stunned'] = True
    return f"{player['name']} used Thunder Strike! {enemy['name']} took {damage} damage and is stunned!"


# Paladin Skills

def heal(player):
    healing = player['magic']
    player['hp'] += healing
    return f"{player['name']} used Heal! Restored {healing} HP!"

def smite(player, enemy):
    damage = player['magic'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Smite! {enemy['name']} took {damage} damage!"

def holyLight(player, enemies):
    healing = player['magic']
    damage = player['magic'] * 0.8
    player['hp'] += healing
    for enemy in enemies:
        if enemy['type'] == 'undead':
            enemy['hp'] -= damage * 2
        else:
            enemy['hp'] -= damage
    return f"{player['name']} used Holy Light! Healed {healing} HP and damaged enemies!"

def divineProtection(player, ally):
    ally['defense'] += player['magic']
    return f"{player['name']} used Divine Protection! {ally['name']}'s defense increased!"

def layHands(player, ally):
    ally['hp'] = ally['max_hp']
    return f"{player['name']} used Lay Hands! {ally['name']} fully healed!"

def judgment(player, enemy):
    damage = player['magic'] * 2
    enemy['hp'] -= damage
    return f"{player['name']} used Judgment! {enemy['name']} took {damage} damage!"

def holyNova(player, allies, enemies):
    healing = player['magic']
    damage = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Holy Nova! Healed allies and damaged enemies!"

def consecrate(player, location):
    # Assuming this creates a zone with ongoing effect
    return f"{player['name']} used Consecrate! The ground at {location} is now consecrated!"

def divineFavor(player):
    player['attack'] *= 1.5
    player['defense'] *= 1.5
    return f"{player['name']} used Divine Favor! Attack and defense significantly increased!"

def guardianAngel(player, ally):
    ally['protected_by_angel'] = True
    return f"{player['name']} used Guardian Angel! {ally['name']} is now protected!"


# Monk Skills

def punch(player, enemy):
    damage = player['attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Punch! {enemy['name']} took {damage} damage!"

def meditate(player):
    player['hp'] += 10
    player['mana'] += 10
    return f"{player['name']} used Meditate! Restored 10 HP and 10 Mana!"

def flurry(player, enemy):
    damage = player['attack'] * 0.8
    for _ in range(3):
        enemy['hp'] -= damage
    return f"{player['name']} used Flurry! {enemy['name']} took {damage * 3} damage!"

def focus(player):
    player['attack'] *= 1.5
    return f"{player['name']} used Focus! Attack significantly increased!"

def zen(player):
    player['hp'] = player['max_hp']
    player['mana'] = player['max_mana']
    return f"{player['name']} used Zen! Fully restored HP and Mana!"

def triplePunch(player, enemy):
    damage = player['attack'] * 0.9
    for _ in range(3):
        enemy['hp'] -= damage
    return f"{player['name']} used Triple Punch! {enemy['name']} took {damage * 3} damage!"

def innerPeace(player):
    player['hp'] += player['max_hp'] * 0.5
    player['mana'] += player['max_mana'] * 0.5
    return f"{player['name']} used Inner Peace! Restored 50% of max HP and Mana!"

def roundhouseKick(player, enemies):
    damage = player['attack']
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Roundhouse Kick! All enemies took {damage} damage!"

def zenMastery(player):
    player['attack'] *= 1.5
    player['defense'] *= 1.5
    player['hp'] += player['max_hp'] * 0.2
    player['mana'] += player['max_mana'] * 0.2
    return f"{player['name']} used Zen Mastery! Increased attack, defense, and partially restored HP and Mana!"

def fistOfTheHeavens(player, enemy):
    damage = player['magic'] * 2
    enemy['hp'] -= damage
    return f"{player['name']} used Fist of the Heavens! {enemy['name']} took {damage} damage!"


# Cleric Skills

def heal(player, target):
    healing = player['magic'] * 1.2
    target['hp'] += healing
    return f"{player['name']} used Heal on {target['name']}! Restored {healing} HP!"

def prayer(player, allies):
    for ally in allies:
        ally['hp'] += player['magic'] * 0.5
    return f"{player['name']} used Prayer! Healed all allies!"

def holyLight(player, target):
    damage = player['magic'] * 1.5
    target['hp'] -= damage
    return f"{player['name']} used Holy Light on {target['name']}! {target['name']} took {damage} damage!"

def bless(player, target):
    target['attack'] *= 1.2
    target['defense'] *= 1.2
    return f"{player['name']} used Bless on {target['name']}! {target['name']}'s attack and defense increased!"

def resurrect(player, target):
    if target['hp'] <= 0:
        target['hp'] = player['magic'] * 2
        return f"{player['name']} used Resurrect on {target['name']}! {target['name']} has been brought back to life!"
    else:
        return f"{player['name']} tried to use Resurrect on {target['name']}, but it was unnecessary!"

def divineFavor(player):
    player['attack'] *= 1.3
    player['defense'] *= 1.3
    return f"{player['name']} used Divine Favor! Attack and defense increased!"

def ward(player, target):
    target['magic_resistance'] += 20
    return f"{player['name']} used Ward on {target['name']}! {target['name']}'s magic resistance increased!"

def divineWrath(player, enemies):
    damage = player['magic'] * 1.4
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Divine Wrath! All enemies took {damage} damage!"

def holyNova(player, allies, enemies):
    healing = player['magic'] * 0.8
    damage = player['magic'] * 0.6
    for ally in allies:
        ally['hp'] += healing
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Holy Nova! Healed allies and damaged enemies!"


# Bard Skills

def sing(player, allies):
    for ally in allies:
        ally['attack'] *= 1.1
        ally['defense'] *= 1.1
    return f"{player['name']} used Sing! All allies' attack and defense increased!"

def inspire(player, allies):
    for ally in allies:
        ally['attack'] *= 1.2
        ally['defense'] *= 1.2
    return f"{player['name']} used Inspire! All allies' attack and defense significantly increased!"

def harmony(player):
    player['status_cleared'] = True
    return f"{player['name']} used Harmony! Cleared negative status effects!"

def dissonance(player, enemies):
    for enemy in enemies:
        enemy['confused'] = True
    return f"{player['name']} used Dissonance! Enemies are confused!"

def ballad(player, allies):
    healing = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    return f"{player['name']} used Ballad! Healed all allies over time!"

def serenade(player, enemy):
    enemy['charmed'] = True
    return f"{player['name']} used Serenade on {enemy['name']}! {enemy['name']} is charmed!"

def requiem(player, enemies):
    for enemy in enemies:
        enemy['sleeping'] = True
    return f"{player['name']} used Requiem! Enemies put to sleep!"

def aria(player, allies):
    for ally in allies:
        ally['magic_resistance'] += 20
    return f"{player['name']} used Aria! All allies' magic resistance increased!"

def duet(player, anotherBard, allies):
    for ally in allies:
        ally['attack'] *= 1.3
        ally['defense'] *= 1.3
    return f"{player['name']} and {anotherBard['name']} performed a Duet! Significantly increased attack and defense for all allies!"

def epicBallad(player, allies):
    for ally in allies:
        ally['hp'] += player['magic'] * 1.5
        ally['mana'] += player['magic'] * 1.5
    return f"{player['name']} performed Epic Ballad! Massively restored HP and Mana for all allies!"


# Ranger Skills

def bowShot(player, enemy):
    damage = player['ranged_attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Bow Shot! {enemy['name']} took {damage} damage!"

def findPath(player):
    player['shortcuts_found'] += 1
    return f"{player['name']} used Find Path! Discovered a shortcut!"

def snipe(player, enemy):
    damage = player['ranged_attack'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Snipe! {enemy['name']} took {damage} damage!"

def animalCompanion(player):
    player['companion_summoned'] = True
    return f"{player['name']} summoned an Animal Companion! Companion aid is at hand!"

def quickShot(player, enemy):
    damage = player['ranged_attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Quick Shot! {enemy['name']} took {damage} damage!"

def camouflage(player):
    player['hidden'] = True
    return f"{player['name']} used Camouflage! Became nearly invisible!"

def track(player, enemy):
    enemy['tracked'] = True
    return f"{player['name']} used Track! {enemy['name']} is now being tracked!"

def longShot(player, enemy):
    distance = player['location'].distanceTo(enemy['location'])
    damage = player['ranged_attack'] * (1 + distance / 10)
    enemy['hp'] -= damage
    return f"{player['name']} used Long Shot! {enemy['name']} took {damage} damage from afar!"

def auraOfHealing(player, allies):
    healing = player['magic'] * 0.5
    for ally in allies:
        ally['hp'] += healing
    return f"{player['name']} activated Aura of Healing! Healed nearby allies!"

def summonFamiliar(player):
    player['familiar_summoned'] = True
    return f"{player['name']} summoned a Familiar! Familiar aid is at hand!"


# General Skills

def attack(player, enemy):
    weapon_dps = player['weapon']['dps']
    damage = player['attack'] * weapon_dps
    enemy['hp'] -= damage
    return f"{player['name']} attacks {enemy['name']} with {player['weapon']['name']} for {damage} damage!"

def dodge(player):
    roll = roll_d20() + player['agility_modifier']
    if roll >= 10:
        player['dodging'] = True
        return f"{player['name']} successfully dodged the next attack!"
    else:
        return f"{player['name']} failed to dodge!"

def rest(player):
    player['hp'] += 10  # Assuming fixed HP recovery
    player['mana'] += 10  # Assuming fixed Mana recovery
    return f"{player['name']} rests, regaining some health and mana."


def dodge(player):
    player['dodging'] = True
    return f"{player['name']} is prepared to dodge the next attack!"


def block(player):
    player['blocking'] = True
    return f"{player['name']} is prepared to block, ready to reduce the next incoming attack's damage by half!"
