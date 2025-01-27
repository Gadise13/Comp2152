
# Gadise Oli
# 101295074

# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# Dice options
diceOptions = list(range(1, 7))

# Function to get valid combat strength input
def get_combat_strength(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Input must be an integer between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 6.")

# Get hero and monster combat strengths
combatStrength = get_combat_strength("Enter your combat strength (1-6): ")
mCombatStrength = get_combat_strength("Enter monster's combat strength (1-6): ")

# Weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Display available weapons
print("Available Weapons:")
for i, weapon in enumerate(weapons, 1):
    print(f"{i}. {weapon}")

# Simulate 10 rounds of battle
for j in range(1, 20, 2):
    if j == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break

    # Roll dice for hero and monster
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    # Add dice roll to combat strengths
    hero_strength = combatStrength + hero_roll
    monster_strength = mCombatStrength + monster_roll

    # Announce selected weapon based on dice roll
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    # Determine the winner of the round
    if hero_strength > monster_strength:
        winner = "Hero"
    elif hero_strength < monster_strength:
        winner = "Monster"
    else:
        winner = "Draw"

    # Print battle details
    print(f"Round {j}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_strength}, Monster Total Strength: {monster_strength}.")
    print(f"{winner} wins the round!\n")

    # --- Nested if statement
    print("You meet the monster. FIGHT!!")
    input("You strike first (Press enter)")

    print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
    if combatStrength >= mHealthPoints:
        mHealthPoints = 0
        print("You've killed the monster")
    else:
        mHealthPoints -= combatStrength
        print("You've reduced the monster's health to: " + str(mHealthPoints))

        print("The monster strikes!!!")
        print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
        if mCombatStrength >= healthPoints:
            healthPoints = 0
            print("You're dead")
        else:
            healthPoints -= mCombatStrength
            print("The monster has reduced your health to: " + str(healthPoints))
