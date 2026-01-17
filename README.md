🛡️ Evil Wizard RPG Battle Game
------------------------------------------
Overview

This is a turn-based role-playing game implemented in Python. Players can choose from multiple character classes, each with unique abilities, and battle against the Evil Wizard in a strategic combat system. The game features attacks, special abilities, shields, evasion, and healing mechanics to provide a tactical experience.
-------------------------------------------

🎮 Character Classes

The game includes four playable classes and one main enemy:

Class	Description	Abilities
Warrior	A strong melee fighter with high health and defensive skills.	Power Strike (extra damage), Shield Block (blocks next attack)
Mage	A ranged spellcaster with high attack power but lower health.	Fireball (extra damage), Magic Shield (blocks next attack)
Archer	A nimble ranged attacker who can deal double damage and evade attacks.	Arrow Rain (double damage), Eagle Eye (evade next attack)
Paladin	A defensive hero with moderate damage and shield abilities.	Holy Strike (bonus damage), Divine Shield (blocks next attack)
Evil Wizard (enemy)	Regenerates health each turn and attacks the player.	Dark Magic (damage), Shadow Shield (blocks next attack)


-----------------------------------

⚔️ Gameplay Mechanics

Turn-Based Combat: Players select actions each turn: attack, use a special ability, heal, or view stats.

Randomized Damage: Attack damage is randomized within a range to create unpredictability.

Special Abilities: Each character has two unique abilities, such as dealing extra damage or blocking attacks.

Healing Mechanic: Players can heal during their turn. Health cannot exceed the maximum limit.

Shield & Evade: Defensive abilities allow characters to block or dodge the next incoming attack.

Evil Wizard Behavior: The enemy regenerates health each turn and attacks the player afterward.

Victory/Defeat Messages: Clear notifications when either the player or the wizard is defeated.

---------------------

🎮 How to Play
1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Run the Game

Make sure you have Python 3.8+ installed, then run:

python3 main.py

---------------------------------------
💻 Files

characters.py – Contains all character classes, abilities, attack and healing logic.

main.py – Handles character selection, turn-based battle system, and user interface.

-----------------------------------------------

🔧 Requirements

Python 3.6+

No external libraries required

-------------------------------------------

🌟 Features

Four unique playable characters with distinct abilities.

Strategic combat with offensive and defensive options.

Centralized healing system to allow flexible recovery.

Randomized attacks for unpredictability.

Functional shield/evade mechanic for tactical gameplay.

Clean, modular, and scalable code architecture.

--------------------------------------------

👨‍💻 Author

Kayla Salmon – Python RPG Project for coding practice and demonstration of OOP concepts, inheritance, and game logic.