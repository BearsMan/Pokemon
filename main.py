
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
pokemom3 = Pokemon("Bulbasaur", "Grass", 45)
pokemon4 = Pokemon("Squirtle", "Water", 44)

listOfPokemon = [pokemon1, pokemon2, pokemom3, pokemon4]
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