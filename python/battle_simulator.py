import json
from pokemon import Pokemon
from pokemon import Moves

pokedex = None
with open('../json/pokedex.json') as f:
   pokedex = json.load(f)

moves = None
with open('../json/moves.json') as f:
   moves = json.load(f)

player1p1 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
player1p2 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

player2p1 = Pokemon(pokedex["zaciancrowned"], [moves["closecombat"]])

#automate pokemon_team list so the list can have every pokemon no the team 
pokemon_team = [player1p1, player1p2]

def interface():
   current_pokemon = 0
   input("Welcome to the Pokémon Battle Simulator. Press enter to continue")
   selection = input("Here is the battle situation: " + player1p1.name + " versus " + player2p1.name + ".\n" + "Your " + player1p1.name + " has " + str(player1p1.hp) + " HP. The opponent's " + player2p1.name + " has " + str(player2p1.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")

   if selection == "A":
      move_selection = input("Pick your move:\n" + str(player1p1.moves))
      pokemon_team[current_pokemon].move(move_selection)
   elif selection == "S":
      switch_selection = input("Here is you team:\n" + print_list(pokemon_team) + "\n" + "You have " + str(len(pokemon_team)))
      current_pokemon = switch_selection - 1

def print_list(l):
   seperator = ", "
   for i in l:
      print(seperator.join(i))




print(interface())