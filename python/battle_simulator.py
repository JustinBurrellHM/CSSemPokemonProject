import json
from python import Pokemon

with open('../json/pokedex.json') as f:
   pokedex = json.load(f)

def interface():
   input("Welcome to the Pokémon Battle Simulator. Press enter to continue")
   input("Here is the battle situation " + "")

print(interface())

'''
p1 = pokemon()
p2 = pokemon()

choose a move 
choose m1
p2.takeDamage(m1)
'''