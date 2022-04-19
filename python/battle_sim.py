from code import interact
import json
import random
from pokemon import Pokemon
from pokemon import Moves
from battlequeue import Battlequeue
from option import Option

class Battle:  
   def __init__(self):
      self.bq = Battlequeue()
      self.pokedex = None
      self.moves = None
      self.current_pokemon = [0, 0]
      self.pokemon = None
      self.pokemon2 = None
      self.game_over = False
      self.round_counter = 1
      self.master = []

      # with open('../json/pokedex.json') as f:
      with open('/Users/justinburrell/Desktop/HM Comp Sci/Comp Sci Sem/Semester Project/CSSemPokemonProject/json/pokedex.json') as f:
         self.pokedex = json.load(f)

      # with open('../json/moves.json') as f:
      with open('/Users/justinburrell/Desktop/HM Comp Sci/Comp Sci Sem/Semester Project/CSSemPokemonProject/json/moves.json') as f:
         self.moves = json.load(f)

      #automate pokemon_team list so the list can have every pokemon no the team 
      pokemon_team = []
      pokemon_team = self.generate_pokemon(5)
      self.master.append(pokemon_team)
      
      pokemon_team2 = []
      pokemon_team2 = self.generate_pokemon(5)
      self.master.append(pokemon_team2)

   def generate_pokemon(self, num_pokemon):
      pokemon_team_list = []
      for _ in range(0,num_pokemon):
         moves_list = []
         random_pokemon_move_names = []
         for _ in range(0,4):
            random_pokemon_move_name = random.choice(list(self.moves))
            while self.moves[random_pokemon_move_name][str("basePower")] == 0:
               random_pokemon_move_name = random.choice(list(self.moves))
            random_pokemon_move_names.append(random_pokemon_move_name)
         for i in random_pokemon_move_names:
            random_pokemon_move = Moves(self.moves[i])
            moves_list.append(random_pokemon_move)
         random_pokemon_name = random.choice(list(self.pokedex))
         random_pokemon_json = self.pokedex[random_pokemon_name]
         random_pokemon = Pokemon(random_pokemon_json, moves_list)
         pokemon_team_list.append(random_pokemon)
      return pokemon_team_list

   def interface(self):

      self.pokemon = self.master[0][self.current_pokemon[0]]
      self.pokemon2 = self.master[1][self.current_pokemon[1]]

      input("Welcome to the Pokémon Battle Simulator. Click enter to continue ")
      while self.game_over == False:
         self.pokemon = self.master[0][self.current_pokemon[0]]
         self.pokemon2 = self.master[1][self.current_pokemon[1]]
         input("\n" + "This is Round #" + str(self.round_counter) + ". Click enter to continue ")
         #code so cpu has already decided whether it wants to attack or switch
         self.get_option()
         self.process_options()
         if self.game_over == True:
               break
         self.round_counter += 1
      self.check_win()

   def print_list(self, l):
      string_pokemon = [str(i) for i in l]
      seperator = ", "
      return seperator.join(string_pokemon)
   
   def get_option(self):
      #ask user if they want to attack or switchb
      selection = input("\n" + "Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")
      if selection == "A":
         move_selection = input("\n" + "Pick your move:\n" + self.print_list(self.pokemon.moves) + " ")
         attack_option = Option(self.pokemon, self.pokemon_team, self.pokemon2, "Attack", self.pokemon, self.pokemon.moves[int(move_selection) -1])
         #save option to battlequeue class
         self.bq.save(attack_option)
      elif selection == "S":
         switch_selection = input("\n" + "Here is you team:\n" + self.print_list(self.pokemon_team) + "\n" + "You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
         switch_option = Option(self.pokemon, self.pokemon_team, self.pokemon2, "Switch", self.pokemon, int(switch_selection) -1)
         #save option to battlequeue class
         self.bq.save(switch_option)
         #or switch   

      #generate cpu move
      selection = input("\n" + "The CPU is deciding its move. Click enter to continue. ")
      random_cpu_selection = random.randint(0,100)
      #percent chances for whether or not cpu attacks or switches
      if random_cpu_selection < 10:
      # if random_cpu_selection < 70:
         cpu_random_move = random.choice(self.pokemon2.moves)
         attack_option = Option(self.pokemon2, self.pokemon_team2, self.pokemon, "Attack", self.pokemon2, cpu_random_move)
         self.bq.save(attack_option)
      else:
         cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
         while cpu_random_switches == self.current_pokemon2:
            cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
         switch_option = Option(self.pokemon2, self.pokemon_team2, self.pokemon, "Switch", self.pokemon2, cpu_random_switches)

         self.bq.save(switch_option)
   
   def process_options(self):
      while self.bq.length() > 0:
         action = self.bq.process()[1]
         #check to see if there is something in pq
         if action == None:
            break
         #exceute move 
         if action.move_type == "Attack":
            self.process_attack(action.agent, action.target, action.pokemon_name, action.pokemon_move)
         elif action.move_type == "Switch":
            self.process_switch(action.agent, action.agent_team, action.pokemon_move)
         
   def process_attack(self, poke, pokemonA, pokemonM, pokemonD):
      '''
      poke = either pokemon or pokemon2
      pokemonA = attacking pokemon
      pokemonM = pokemon move
      pokemonD = defending pokemon/getting attacked
      '''
      poke.move(pokemonM, pokemonD)
      print("\n" pokemonA + " just used " + str(pokemonM) + " on " + pokemonD+ "!")

   def process_switch(self, poke_index, poke_team, switch_index):
      '''
      poke = either pokemon or pokemon2
      poke_team = pokemon team
      switch_index = index 
      '''
      self.current_pokemon[poke_index] = switch_index
      poke = self.master[poke_index][self.current_pokemon[switch_index]]
      print("\n" + "You just switched to " + poke + " !")

   def switch_pokemon(self, n = -1):
      if n == -1:
         switch_selection = input("\n" + "Here is you team:\n" + self.print_list(self.pokemon_team) + "\n" + "You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
         self.current_pokemon = int(switch_selection) - 1
         self.pokemon = self.pokemon_team[self.current_pokemon]
         print("\n" + "You just switched to " + self.pokemon.name + " !")
      else:
         self.current_pokemon = int(n) - 1
         self.pokemon = self.pokemon_team[self.current_pokemon]
         print("\n" + "You just switched to " + self.pokemon.name + " !")
   
   def check_health(self):
      #check for health
      if self.pokemon.hp <= 0:
         dead_pokemon_name = self.pokemon.name
         del self.pokemon_team[self.current_pokemon]
         if len(self.pokemon_team) == 0:
            self.game_over = True
         else:
            dead_pokemon_switch = input("\n" + "Your " + dead_pokemon_name + " has fainted. You have " + str(len(self.pokemon_team)) + " pokemon avaliable." + "\n" + "Here is you team: " + self.print_list(self.pokemon_team) + "\n" + "Pick the pokemon you want to switch to ")
            self.switch_pokemon(dead_pokemon_switch)
         
   #cpu-based functions
   def cpu_switch_pokemon(self, fainted = False):
      cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
      while cpu_random_switches == self.current_pokemon2:
         cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
      self.current_pokemon2 = cpu_random_switches
      self.pokemon2 = self.pokemon_team2[self.current_pokemon2]
      if fainted == False:
         print("\n" + "The CPU just switched to " + self.pokemon2.name + " !")
   
   def cpu_check_health(self):
      #check for health
      if self.pokemon2.hp <= 0:
         dead_pokemon_name2 = self.pokemon2.name
         del self.pokemon_team2[self.current_pokemon2]
         if len(self.pokemon_team2) == 0:
            self.game_over = True
         else:
            self.current_pokemon2 = -1
            self.cpu_switch_pokemon(True)
            print("\n" + "The CPUs' " + dead_pokemon_name2 + " has fainted! They switched to " + self.pokemon2.name)

      #check for team
         
   def check_win(self):
      #if cpu won
      if len(self.pokemon_team) == 0:
         print("\n" + "Game Over! You Lost in " + str(self.round_counter) + " rounds.")
      #if user won
      elif len(self.pokemon_team2) == 0:
         print("\n" + "Game Over! You Won in " + str(self.round_counter) + " rounds.")

game = Battle()
game.interface() 