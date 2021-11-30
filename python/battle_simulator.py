import json
from pokemon import Pokemon

pokedex = None
with open('../json/pokedex.json') as f:
   pokedex = json.load(f)

p1 = Pokemon(pokedex["zaciancrowned"])
p2 = Pokemon(pokedex["zaciancrowned"])

def __str__(self):
   return self.name + self.pokemon_hp + self.pokemon_atk + self.pokemon_def + self.pokemon_spa + self.pokemon_spd + self.pokemon_spe + self.moves

   f"Name: {self.name} "

def interface():
   input("Welcome to the Pokémon Battle Simulator. Press enter to continue")
   print(p1.__str__())
   # input("Here is the battle situation " + p1 + "versus" + p2)


print(interface())



# choose a move 
# choose m1
# p2.takeDamage(m1)