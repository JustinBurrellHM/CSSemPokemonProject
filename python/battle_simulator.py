import json

with open('pokedex.json') as f:
   pokedex = json.load(f)

pokemon1 = pokedex["venusaur"]
pokemon2 = pokedex["aegislash"]

def interface():
   input("Welcome to the Pokémon Battle Simulator. Press enter to continue")

print(interface())





