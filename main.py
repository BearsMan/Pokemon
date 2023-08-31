# create Pokemon Game
# Setup Classes, Variables, Functions, etc.
import random

class Pokemon:

 def __init__(self, name, type, health):
   self.name = name
   self.type = type
   self.health = health

class Attack:

 def __init__(self, name, damage, attackType):
   self.name = name
   self.damage = damage
   self.attack = attackType

pokemon1 = Pokemon("Pikachu", "eletric", 35)
pokemon2 = Pokemon("Charizard", "fire", 78)
pokemon3 = Pokemon("Bulbasaur", "Grass", 45)
pokemon4 = Pokemon("Squirtle", "Water", 44)

listOfPokemon = [pokemon1, pokemon2, pokemon3, pokemon4]
Attack1 = Attack("Thunder", 110, "Eletric")
Attack2 = Attack("Steel", 100, "Steel")
Attack3 = Attack("Quick Attack", 40, "Normal")
Attack4 = Attack("Inferno", 100, "Fire")
Attack5 = Attack("Growl", 0, "Normal")
Attack6 = Attack("Dragon Tail", 60, "Dragon")
Attack7 = Attack("Vine Whip", 45, "Grass")
Attack8 = Attack("Razor Leaf", 55, "Grass")
Attack9 = Attack("Solar Beam", 120, "Grass")
Attack10 = Attack("Water Gun", 40, "Water")
Attack11 = Attack("Water Pulse", 60, "Water")
Attack12 = Attack("Hydro Pump", 110, "Water")

def battleAttack(pokemon, attack, targetPokemon):
  damageCheck = False
  print(pokemon.name + "used" + attack.name)
  while (damageCheck == False):
    superEffective = 0
    if attack.attackType == "fire" and targetPokemon.type == "water":
      print(attack.name + "Was not very effective")
      superEffective = -15
    if attack.attackType == "water" and targetPokemon.type == "fire":
      print(attack.name + "Was very effective")
      
    if attack.attackType == "steel" and attack.attackType == "water":
        print(attack.name + "was or was not effective")
        superEffective = -15
    if attack.attackType == "steel" and targetPokemon.type == "water":
        print(attack.name + "Attack is not very effective ")
    if attack.AttackType == "water" and targetPokemon.type == "steel":
      print(attack.name + "Attack is not very effective ")
      superEffective = -10
    if attack.AttackType == "Eletric" and targetPokemon.type == "water":
      print(attack.name + "Attack is super effetive")
      superEffective = 15 + 5
    if attack.AttackType == "water" and targetPokemon.type == "Eletric":
      print(attack.name + "Attack is not super effetive")
  
    targetPokemon.health -= Attack.damage + superEffective
    print(targetPokemon.name + "took" + str(attack.damage + superEffective)+ "damage!")
    damageCheck = True

print("welcome to my pokemon game, choose a pokemon of your choice. \n 1. Squirtle \n 2. Charmander \n 3. Bulbasaur \n 4. Pikachu")

pokemon_choice = int(input())
if pokemon_choice == 1:
  print("You chose Squirtle!")
  playerPokemon = Pokemon("Squirtle", "Water", 44)
  listOfMoves = [Attack10, Attack11, Attack12]

if pokemon_choice == 2:
  print("You chose Charizard!")
  playerPokemon = Pokemon("Charizard", "fire", 78)
  listOfMoves = [Attack4, Attack5, Attack6]

if pokemon_choice == 3:
  print("You chose Bulbasaur")
  playerPokemon = Pokemon("Bulbasaur", "Grass", 45)
  listOfMoves = [Attack7, Attack8, Attack9]

if pokemon_choice == 4:
  print("You chose Pickchu!")
  playerPokemon = Pokemon("Pikachu", "eletric", 35)
  listOfMoves = [Attack1, Attack2, Attack3]

enemyChoice = random.randint(0, 3)
enemyPokemon = listOfPokemon[enemyChoice]
if enemyChoice == 0:
   print("The enemy chose Squirtle!")

   enemyPokemon = pokemon4
   listOfEnemyMoves = [Attack10, Attack11, Attack12]

if enemyChoice == 1:
   print("The enemy chose Charizard!")
   enemyPokemon = pokemon2
   listOfEnemyMoves = [Attack4, Attack5, Attack6]

if enemyChoice == 2:
   print("The enemy chose Bulbasaur!")
   enemyPokemon = pokemon3
   listOfEnemyMoves = [Attack7, Attack8, Attack9]

if enemyChoice == 3:
   print("The enemy chose Pikachu!")
   enemyPokemon = pokemon4
   listOfEnemyMoves = [Attack1, Attack2, Attack3]

print("The battle begins with "  + playerPokemon.name +  " and "  + enemyPokemon.name)
battleLoop = True

while battleLoop:
  attackChoice = int(input("Enter what number of move that you to enter!"))
  Attack(playerPokemon, listOfMoves[attackChoice], enemyPokemon)
  if enemyPokemon.health <= 0:
    print("You Win!")
    break
    
  enemyAttack = random.randint(0, 2)
  Attack(enemyPokemon, listOfEnemyMoves[enemyAttack], playerPokemon)
  if playerPokemon.health <= 0:
    print("You Lose!")
    break

print("The player has" + str(playerPokemon.health) + "Remaining")