#ClassDatabase.py

# Extending the game database to include more skills and spells for each class.
# Each class will have a list of skills and spells that unlock at each level up to level 10.

game_database_python_extended = {
    "classes": {
        "Warrior": {
            "base_hp": 30,
            "base_attack": 5,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Charge", "Defend"],
                "2": ["ShieldBash"],
                "3": ["Cleave"],
                "4": ["Fortify"],
                "5": ["Whirlwind"],
                "6": ["StoneSkin"],
                "7": ["BladeDance"]
            }
        },
        "Rogue": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["Stealth", "Backstab"],
                "2": ["ShadowStrike"],
                "3": ["Ambush"],
                "4": ["Evasion"],
                "5": ["Assassinate"],
                "6": ["Vanish"],
                "7": ["Lacerate"]
            }
        },
        "Mage": {
            "base_hp": 20,
            "base_attack": 7,
            "base_defense": 3,
            "level_up_skills": {
                "1": ["Fireball", "Teleport"],
                "2": ["ArcaneBlast"],
                "3": ["ElementalShield"],
                "4": ["ManaBurn"],
                "5": ["Blink"],
                "6": ["NetherPortal"],
                "7": ["Phase"],
                "8": ["SummonElemental"],
                "9": ["ThunderStrike"]
            }
        },
        "Paladin": {
            "base_hp": 35,
            "base_attack": 4,
            "base_defense": 6,
            "level_up_skills": {
                "1": ["Heal", "Smite"],
                "2": ["HolyLight"],
                "3": ["DivineProtection"],
                "4": ["LayHands"],
                "5": ["Judgment"],
                "6": ["HolyNova"],
                "7": ["Consecrate"],
                "8": ["DivineFavor"],
                "9": ["GuardianAngel"]
            }
        },
        "Monk": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Punch", "Meditate"],
                "2": ["Flurry"],
                "3": ["Focus"],
                "4": ["Zen"],
                "5": ["TriplePunch"],
                "6": ["InnerPeace"],
                "7": ["RoundhouseKick"],
                "8": ["ZenMastery"],
                "9": ["FistOfTheHeavens"]
            }
        },
        "Cleric": {
            "base_hp": 30,
            "base_attack": 4,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Heal", "Prayer"],
                "2": ["HolyLight"],
                "3": ["Bless"],
                "4": ["Resurrect"],
                "5": ["DivineFavor"],
                "6": ["Ward"],
                "7": ["DivineWrath"],
                "8": ["HolyNova"]
            }
        },
        "Bard": {
            "base_hp": 24,
            "base_attack": 5,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["Sing", "Inspire"],
                "2": ["Harmony"],
                "3": ["Dissonance"],
                "4": ["Ballad"],
                "5": ["Serenade"],
                "6": ["Requiem"],
                "7": ["Aria"],
                "8": ["Duet"],
                "9": ["EpicBallad"]
            }
        },
        "Ranger": {
            "base_hp": 28,
            "base_attack": 6,
            "base_defense": 4,
            "level_up_skills": {
                "1": ["BowShot", "FindPath"],
                "2": ["Snipe"],
                "3": ["AnimalCompanion"],
                "4": ["QuickShot"],
                "5": ["Camouflage"],
                "6": ["Track"],
                "7": ["LongShot"],
                "8": ["AuraOfHealing"],
                "9": ["SummonFamiliar"]
            }
        }
    }
}


skill_descriptions = {
    # Warrior skills
    "Charge": "Rush towards an enemy, dealing extra damage on the next attack.",
    "Defend": "Increase your defense, reducing damage from the next attack against you.",
    "ShieldBash": "Use your shield to bash an enemy, causing a stun effect.",
    "Cleave": "Swing your weapon in a wide arc, hitting multiple enemies.",
    "Fortify": "Strengthen your armor, reducing incoming physical damage.",
    "Whirlwind": "Perform a spinning attack that hits multiple enemies around you.",
    "StoneSkin": "Transform your skin into stone, massively boosting your defense for a short time.",
    "BladeDance": "Engage in a deadly dance, striking all enemies around you multiple times.",
    # Rogue skills
    "Stealth": "Become invisible to enemies, making it easier to avoid combat or land the first strike.",
    "Backstab": "Perform a sneak attack that deals critical damage.",
    "ShadowStrike": "Strike from the shadows, dealing extra damage and applying a bleed effect.",
    "Ambush": "Set up an ambush, gaining the initiative in the next combat.",
    "Evasion": "Dodge the next attack against you, avoiding its damage.",
    "Assassinate": "Attempt to kill an enemy in one shot. Higher success rate on weaker enemies.",
    "Vanish": "Disappear from sight, avoiding all attacks for a short time.",
    "Lacerate": "Cause a deep wound on the enemy, causing them to bleed over time.",
    # Mage skills
    "Fireball": "Cast a fireball that deals AoE (Area of Effect) damage.",
    "Teleport": "Instantly move to a different location within a short distance.",
    "ArcaneBlast": "Release a burst of arcane energy, damaging enemies in a radius.",
    "ElementalShield": "Summon a shield of elemental energy, reducing incoming elemental damage.",
    "ManaBurn": "Burn an enemy's mana, dealing damage equal to the amount burned.",
    "Blink": "Teleport a short distance, even through walls.",
    "NetherPortal": "Open a portal to the nether realm, summoning demons to aid you.",
    "Phase": "Phase out of reality, avoiding all damage for a short time.",
    "SummonElemental": "Summon an elemental to fight for you.",
    "ThunderStrike": "Call down a bolt of lightning, dealing heavy damage to a single enemy.",
    # Paladin skills
    "Heal": "Restore a portion of HP to yourself or an ally.",
    "Smite": "Channel divine energy to deal extra damage on your next attack.",
    "HolyLight": "Summon a beam of holy light, healing allies and damaging undead enemies.",
    "DivineProtection": "Grant an ally a shield that absorbs a certain amount of damage.",
    "LayHands": "Lay your hands on an ally, fully restoring their HP.",
    "Judgment": "Pass divine judgment on an enemy, dealing heavy damage.",
    "HolyNova": "Emit a burst of holy light, healing allies and damaging enemies.",
    "Consecrate": "Consecrate the ground, causing damage to enemies who step on it.",
    "DivineFavor": "Gain the favor of the gods, increasing the effectiveness of your next spell.",
    "GuardianAngel": "Summon a guardian angel that protects an ally from the next fatal attack.",
    # Monk skills
    "Punch": "A quick and basic melee attack.",
    "Meditate": "Enter a state of deep focus, restoring some HP and Mana.",
    "Flurry": "Perform a series of quick punches, dealing damage to a single enemy.",
    "Focus": "Enter a focused state, increasing your next attack's damage.",
    "Zen": "Enter a Zen state, regaining full HP and Mana.",
    "TriplePunch": "Perform a triple punch combo, dealing heavy damage.",
    "InnerPeace": "Find inner peace, rapidly regenerating HP and Mana for a short time.",
    "RoundhouseKick": "Perform a roundhouse kick, hitting multiple enemies.",
    "ZenMastery": "Achieve the pinnacle of Zen mastery, making all your skills more potent.",
    "FistOfTheHeavens": "Summon a giant fist from the heavens to smash your enemies.",
    # Cleric Skills
    "Heal": "Restore a portion of HP to yourself or an ally.",
    "Prayer": "Say a prayer, granting a temporary buff to all party members.",
    "HolyLight": "Summon a beam of holy light, healing allies and damaging undead enemies.",
    "Bless": "Bless an ally, granting them a temporary boost to their abilities.",
    "Resurrect": "Bring an ally back to life with a portion of their HP.",
    "DivineFavor": "Gain the favor of the gods, increasing the effectiveness of your next spell.",
    "Ward": "Place a magical ward on an ally, granting resistance to magical attacks.",
    "DivineWrath": "Unleash the wrath of the gods, dealing massive damage to multiple enemies.",
    "HolyNova": "Emit a burst of holy light, healing allies and damaging enemies.",
    # Bard Skills
    "Sing": "Perform a song that grants temporary bonuses to your party.",
    "Inspire": "Motivate your allies, granting them a temporary boost in combat effectiveness.",
    "Harmony": "Play a harmonious tune, removing negative status effects from your party.",
    "Dissonance": "Play a dissonant tune, causing confusion among enemy ranks.",
    "Ballad": "Play a ballad that heals your party over time.",
    "Serenade": "Perform a serenade, charming an enemy to fight for you temporarily.",
    "Requiem": "Play a haunting melody, putting enemies to sleep.",
    "Aria": "Perform an aria that grants long-lasting buffs to your team.",
    "Duet": "Perform a duet with another Bard, combining the effects of both songs.",
    # Ranger Skills
    "BowShot": "Shoot an arrow from a distance, dealing damage to a single enemy.",
    "FindPath": "Discover hidden paths or shortcuts, reducing the time spent on travel.",
    "Snipe": "Take careful aim, dealing extra damage on your next bow shot.",
    "AnimalCompanion": "Summon an animal companion to assist you in combat.",
    "QuickShot": "Shoot an arrow quickly, reducing the time before your next action.",
    "Camouflage": "Blend into your surroundings, becoming nearly invisible.",
    "Track": "Track an enemy, revealing their location.",
    "LongShot": "Take a long-distance shot with your bow, dealing damage based on distance."
}
