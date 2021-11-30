import json
from pokemon import Pokemon

pokedex = None
with open('../json/pokedex.json') as f:
   pokedex = json.load(f)

moves = None
with open('../json/moves.json') as f:
   moves = json.load(f)

p1 = Pokemon(pokedex["zaciancrowned"], [moves["quickattack"]])
p2 = Pokemon(pokedex["zaciancrowned"], [moves["quickattack"]])

def interface():
   input("Welcome to the Pokémon Battle Simulator. Press enter to continue")
   print(p1.name)
   # input("Here is the battle situation " + p1 + "versus" + p2)


print(interface())



# choose a move 
# choose m1
# p2.takeDamage(m1)