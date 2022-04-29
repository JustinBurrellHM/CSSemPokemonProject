import json
import os
import pickle
import random
from code import interact

from dotenv import load_dotenv

load_dotenv()


from battlequeue import Battlequeue
from option import Option
from pokemon import Moves, Pokemon


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
      self.pickled_moveset = None

      #how to load and use the pickled object/dictionary
      pickle_in = open("pokemon_moves.pickle", "rb")
      self.pickled_moveset = pickle.load(pickle_in)
      pickle_in.close()

      with open(os.getenv('pokedex')) as f:
      #with open("json/pokedex.json") as f:
         self.pokedex = json.load(f)

      with open(os.getenv('moves')) as f:
      #with open(json/pokedex.json) as f:
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
         # random_pokemon_name = random.choice(list(self.pokedex))
         random_pokemon_name = random.choice(list(self.pickled_moveset))

         #Case Issue: Sometimes a random pokemon is picked and it has no moves, gives an "IndexError: Cannot choose from an empty sequence" error when trying to run line 76: random_pokemon_move = random.choice(self.pickled_moveset[random_pokemon_name])
         while len(self.pickled_moveset[random_pokemon_name]) == 0:
            random_pokemon_name = random.choice(list(self.pickled_moveset))

         # Case Issue: issues generating minior because there are different colors and they are referred to diferently in the api and showdown json
         while "minior" in random_pokemon_name:
            random_pokemon_name = random.choice(list(self.pickled_moveset))

         #Case Issue: The base zygarde, zygarde 50%, is refered to as zygarde50 in the api but just zygarde50 in the showdown json
         while "zygarde-50" in random_pokemon_name:
            random_pokemon_name = random.choice(list(self.pickled_moveset))

         # print(random_pokemon_name)
         for _ in range(0,4):
            random_pokemon_move = random.choice(self.pickled_moveset[random_pokemon_name])
            random_pokemon_move_names.append(random_pokemon_move)
         #parse and got its respective object
         for move in random_pokemon_move_names:
            if "-" in move:
               move = move.replace("-", "")
            random_pokemon_move = Moves(self.moves[move])
            moves_list.append(random_pokemon_move)
         #parse pokemon name
         if "-" in random_pokemon_name:
            random_pokemon_name = random_pokemon_name.replace("-", "")
         #getting pokemon object
         random_pokemon_json = self.pokedex[random_pokemon_name]
         random_pokemon = Pokemon(random_pokemon_json, moves_list)
         pokemon_team_list.append(random_pokemon)
      return pokemon_team_list

         # for _ in range(0,4):
         #    random_pokemon_move_name = random.choice(list(self.moves))
         #    while self.moves[random_pokemon_move_name][str("basePower")] == 0:
         #       random_pokemon_move_name = random.choice(list(self.moves))

   def interface(self):
      input("Welcome to the Pokémon Battle Simulator. Click enter to continue ")
      while self.game_over == False:
         self.pokemon = self.master[0][self.current_pokemon[0]]
         self.pokemon2 = self.master[1][self.current_pokemon[1]]
         input("\n" + "This is Round #" + str(self.round_counter) + ". Click enter to continue ")
         #code so cpu has already decided whether it wants to attack or switch
         self.get_option()
         self.process_options()
         self.round_counter += 1

   def print_list(self, l):
      string_pokemon = [str(i) for i in l]
      seperator = ", "
      return seperator.join(string_pokemon)
   
   def get_option(self):
      #ask user if they want to attack or switchb
      selection = input("\n" + "Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")
      if selection == "A":
         move_selection = input("\n" + "Pick your move:\n" + self.print_list(self.pokemon.moves) + " ")
         option_dictionary = {"agent": self.pokemon,  "target": 1, "move_type": "Attack", "pokemon_name": self.pokemon, "pokemon_move": self.pokemon.moves[int(move_selection) -1]}
         attack_option = Option(option_dictionary)
         #save option to battlequeue class
         self.bq.save(attack_option)
      elif selection == "S":
         switch_selection = input("\n" + "Here is you team:\n" + self.print_list(self.master[0]) + "\n" + "You have " + str(len(self.master[0])) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
         option_dictionary = {"agent": self.pokemon, "move_type": "Switch", "pokemon_name": self.pokemon, "pokemon_switch_index": int(switch_selection) -1, "agent_index": 0}
         switch_option = Option(option_dictionary)
         #save option to battlequeue class
         self.bq.save(switch_option)
         #or switch   

      #generate cpu move
      selection = input("\n" + "The CPU is deciding its move. Click enter to continue. ")
      random_cpu_selection = random.randint(0,100)
      #percent chances for whether or not cpu attacks or switches
      # if random_cpu_selection < 100:
      if random_cpu_selection < 70:
         cpu_random_move = random.choice(self.pokemon2.moves)
         option_dictionary = {"agent": self.pokemon2,  "target": 0, "move_type": "Attack", "pokemon_name": self.pokemon2, "pokemon_move": cpu_random_move}
         attack_option = Option(option_dictionary)
         self.bq.save(attack_option)
      else:
         cpu_random_switches = random.randint(0, len(self.master[1])-1)
         while cpu_random_switches == self.current_pokemon[1]:
            cpu_random_switches = random.randint(0, len(self.master[1])-1)
         option_dictionary = {"agent": self.pokemon2, "move_type": "Switch", "pokemon_name": self.pokemon2, "pokemon_switch_index": cpu_random_switches, "agent_index": 1}
         switch_option = Option(option_dictionary)
         self.bq.save(switch_option)
   
   def process_options(self):
      while self.bq.length() > 0:
         action = self.bq.process()
         info = action.options
         #check to see if there is something in pq
         if action == None:
            break
         #exceute move 
         if info["move_type"] == "Attack":
            self.process_attack(info["agent"], info["pokemon_name"], info["pokemon_move"], info["target"])
         elif info["move_type"] == "Switch":
            self.process_switch(info["agent_index"], info["pokemon_switch_index"], info['agent'])
         death_check = self.check_health()
         if death_check:
            self.check_win()
            break
         
   def process_attack(self, poke, pokemonA, pokemonM, target):
      '''
      poke = either pokemon or pokemon2
      pokemonA = attacking pokemon
      pokemonM = pokemon move
      pokemonD = defending pokemon/getting attacked
      '''

      pokemonD = self.master[target][self.current_pokemon[target]]
      print("\n" + str(pokemonA) + " just used " + str(pokemonM) + " on " + str(pokemonD) + "!")
      poke.move(pokemonM, pokemonD) 
      self.pokemon = self.master[0][self.current_pokemon[0]]
      self.pokemon2 = self.master[1][self.current_pokemon[1]]
   
   def process_switch(self, poke_index, switch_index, agent):
      '''
      poke = either pokemon or pokemon2
      poke_team = pokemon team
      switch_index = index 
      agent = CPU or User
      '''
      self.current_pokemon[poke_index] = switch_index
      agent = self.master[poke_index][self.current_pokemon[poke_index]]

      if poke_index == 0:
         print("\n" + "You just switched to " + agent.name + " !")
      else:
         print("\n" + "The CPU just switched to " + agent.name + " !")
      self.pokemon = self.master[0][self.current_pokemon[0]]
      self.pokemon2 = self.master[1][self.current_pokemon[1]]
   
   def check_health(self):
      death_check = False
      for (agent,pokemon_index) in enumerate(self.current_pokemon):
         pokemon = self.master[agent][pokemon_index]
         if pokemon.hp <= 0:
            dead_pokemon_name = pokemon.name
            del self.master[agent][self.current_pokemon[agent]]
            if len(self.master[agent]) == 0:
               self.game_over = True
               death_check = True
            else:
               if agent == 0:
                  dead_pokemon_switch = input("\n" + "Your " + dead_pokemon_name + " has fainted. You have " + str(len(self.master[0])) + " pokemon avaliable." + "\n" + "Here is you team: " + self.print_list(self.master[0]) + "\n" + "Pick the pokemon you want to switch to: ")
                  self.current_pokemon[agent] = (int(dead_pokemon_switch) -1)
                  new_pokemon = self.master[agent][self.current_pokemon[agent]] #out of range?
                  print("\n" + 'Your ' + dead_pokemon_name + " has fainted! You switched to " + new_pokemon.name)
                  death_check = True
               else:
                  cpu_random_switches = random.randint(0, len(self.master[1])-1)
                  if len(self.master[1]) == 1:
                     cpu_random_switches = 0
                  else:
                     while cpu_random_switches == self.current_pokemon[1]:
                        cpu_random_switches = random.randint(0, len(self.master[1])-1)
                  self.current_pokemon[agent] = cpu_random_switches
                  new_pokemon = self.master[agent][self.current_pokemon[agent]] #out of range?
                  print("\n" + "The CPUs ' " + dead_pokemon_name + " has fainted! They switched to " + new_pokemon.name)
                  death_check = True
      return death_check
         
   def check_win(self):
      #if cpu won
      if len(self.master[0]) == 0:
         print("\n" + "Game Over! You Lost in " + str(self.round_counter) + " rounds.")
      #if user won
      elif len(self.master[1]) == 0:
         print("\n" + "Game Over! You Won in " + str(self.round_counter) + " rounds.")

battle_sim = Battle()
battle_sim.interface() 
