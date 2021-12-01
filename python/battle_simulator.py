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

player2p1 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
player2p2 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

#automate pokemon_team list so the list can have every pokemon no the team 
pokemon_team = [player1p1, player1p2]

pokemon_team2 = [player2p1, player2p2]

def interface():
   current_pokemon = 0
   current_pokemon2 = 0
   pokemon = pokemon_team[current_pokemon]
   pokemon2 = pokemon_team2[current_pokemon2]
   game_over = False

   while game_over == False:
      input("Welcome to the Pokémon Battle Simulator. Press enter to continue ")
      selection = input("Here is the battle situation: " + pokemon.name + " versus " + pokemon2.name + ".\n" + "Your " + pokemon.name + " has " + str(pokemon.hp) + " HP. The opponent's " + pokemon2.name + " has " + str(pokemon2.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")

      if selection == "A":
         move_selection = input("Pick your move:\n" + str(pokemon.moves))
         pokemon.move(move_selection)
         
         #check for health

         #check for team

      elif selection == "S":
         switch_selection = input("Here is you team:\n" + print_list(pokemon_team) + "\n" + "You have " + str(len(pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
         current_pokemon == int(switch_selection) - 1
      
   print("Game Over!")

def print_list(l):
   string_pokemon = [str(i) for i in l]
   seperator = ", "
   return seperator.join(string_pokemon)

print(interface())