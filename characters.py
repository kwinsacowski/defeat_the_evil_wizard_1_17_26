import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.evade_next = False    # For evade/shield mechanic
        self.shield_active = False
        self.abilities = []  # ability list and allows for additional abilities in the future
        self.ability_names = []

    def attack(self, opponent):
        if opponent.evade_next or opponent.shield_active:
            print(f"{opponent.name} evades the attack!")
            opponent.evade_next = False  # Reset evade status
            opponent.shield_active = False  # Reset shield status
            return
        
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage! curent health of {opponent.name} is {opponent.health}/{opponent.max_health}")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def use_ability(self, ability_number, opponent):
        try:
            self.abilities[ability_number - 1](opponent)
        except IndexError:
            print("Invalid ability choice!")

    def heal(self, amount=20):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.ability_names = ["Power Strike", "Shield Block"]
        self.abilities = [self.power_strike, self.shield_block]

    def power_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Power Strike! Deals {damage} damage!")

    def shield_block(self, opponent):
        self.shield_active = True
        print(f"{self.name} uses Shield Block! Will block the next attack.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.ability_names = ["Fireball", "Magic Shield"]
        self.abilities = [self.fireball, self.magic_shield]

    def fireball(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} casts Fireball! Deals {damage} damage!")

    def magic_shield(self, opponent):
        self.shield_active = True
        print(f"{self.name} casts Magic Shield! Will block the next attack.")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.ability_names = ["Arrow Rain", "Eagle Eye"]
        self.abilities = [self.arrow_rain, self.eagle_eye]

    def arrow_rain(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Arrow Rain! Deals {damage} damage!")

    def eagle_eye(self, opponent):
        self.evade_next = True
        print(f"{self.name} uses Eagle Eye! Will evade the next attack!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.ability_names = ["Holy Strike", "Divine Shield"]
        self.abilities = [self.holy_strike, self.divine_shield]

    def holy_strike(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike! Deals {damage} damage!")

    def divine_shield(self, opponent):
        self.shield_active = True
        print(f"{self.name} uses Divine Shield! Will block the next attack!")


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.ability_names = ["Dark Magic", "Shadow Shield"]
        self.abilities = [self.dark_magic, self.shadow_shield]

    def dark_magic(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses Dark Magic! Deals {damage} damage!")

    def shadow_shield(self, opponent):
        self.shield_active = True
        print(f"{self.name} uses Shadow Shield! Will block the next attack!")

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")