import json
import random
from pokemon import Pokemon
from pokemon import Moves

class Battle:
   def __init__(self):
      self.pokedex = None
      self.moves = None
      self.current_pokemon = 0
      self.pokemon = None
      self.pokemon2 = None
      self.game_over = False
      self.pokemon_team = []
      self.pokemon_team2 = []
      self.round_counter = 1

      with open('../json/pokedex.json') as f:
         pokedex = json.load(f)

      with open('../json/moves.json') as f:
         moves = json.load(f)

      player1p1 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
      player1p2 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

      player2p1 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
      player2p2 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

      #automate pokemon_team list so the list can have every pokemon no the team 
      self.pokemon_team = [player1p1, player1p2]

      self.pokemon_team2 = [player2p1, player2p2]
   
   '''
   def queue(self):
   '''
   
   def interface(self):
      self.current_pokemon = 0
      self.current_pokemon2 = 0
      self.pokemon = self.pokemon_team[self.current_pokemon]
      self.pokemon2 = self.pokemon_team2[self.current_pokemon2]

      input("Welcome to the Pokémon Battle Simulator. Click enter to continue ")
      while self.game_over == False:
         input("\n" + "This is Round #" + str(self.round_counter) + ". Click enter to continue ")
         #code so cpu has already decided whether it wants to attack or switch

         if self.pokemon.spe > self.pokemon2.spe:
            self.user_selection()
            self.cpu_selection()
         elif self.pokemon.spe < self.pokemon2.spe:
            self.cpu_selection()
            self.user_selection()
         elif self.pokemon.spe == self.pokemon2.spe:
            #add randomness, a 50/50 chance for who goes first
            random_speed_counter = random.randint(0,1)
            if random_speed_counter == 0:
               self.user_selection()
               self.cpu_selection()
            if random_speed_counter == 1:
               self.cpu_selection()
               self.user_selection()
         self.round_counter += 1
      self.check_win()

   def print_list(self, l):
      string_pokemon = [str(i) for i in l]
      seperator = ", "
      return seperator.join(string_pokemon)

   #user-based functions
   def user_selection(self):
      selection = input("\n" + "Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")
      if selection == "A":
         self.attack_pokemon()
      elif selection == "S":
         self.switch_pokemon()
   
   def attack_pokemon(self):
      move_selection = input("\n" + "Pick your move:\n" + self.print_list(self.pokemon.moves) + " ")
      current_move = self.pokemon.moves[int(move_selection) - 1]
      self.pokemon.move(current_move, self.pokemon2)
      print("\n" + "Your " + self.pokemon.name + " just used " + str(current_move) + " on " + self.pokemon2.name + "!")
      self.cpu_check_health()

   def switch_pokemon(self):
      switch_selection = input("\n" + "Here is you team:\n" + self.print_list(self.pokemon_team) + "\n" + "You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
      self.current_pokemon = int(switch_selection) - 1
      self.pokemon = self.pokemon_team[self.current_pokemon]
      print("\n" + "You just switched to " + self.pokemon.name + " !")
   
   def check_health(self):
      #check for health
         if self.pokemon.hp == 0:
            dead_pokemon_name = self.pokemon.name
            del self.pokemon_team[self.current_pokemon]
            dead_pokemon_switch = input("\n" + "Your " + dead_pokemon_name + " has died. You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to.")
            self.switch_pokemon()
      #check for team
         if len(self.pokemon_team) == 0:
            self.game_over = True
   
   #cpu-based functions
   def cpu_selection(self):
      selection = input("\n" + "Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "The CPU is deciding its move. Click enter to continue. ")
      random_cpu_selection = random.randint(0,100)
      #percent chances for whether or not cpu attacks or switches
      if random_cpu_selection < 70:
         self.cpu_attack_pokemon()

      else:
         self.cpu_switch_pokemon()
   
   def cpu_attack_pokemon(self):
      cpu_random_move = random.choice(self.pokemon2.moves)
      self.pokemon2.move(cpu_random_move, self.pokemon)
      print("\n" + "The CPUs' " + self.pokemon2.name + " just used " + str(cpu_random_move) + " on " + "your " + self.pokemon.name + "!")
      self.check_health()

   def cpu_switch_pokemon(self):
      cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
      while cpu_random_switches == self.current_pokemon2:
         cpu_random_switches = random.randint(0, len(self.pokemon_team2)-1)
      self.current_pokemon2 = cpu_random_switches
      self.pokemon2 = self.pokemon_team2[self.current_pokemon2]
      print("\n" + "The CPU just switched to " + self.pokemon2.name + " !")
   
   def cpu_check_health(self):
      #check for health
         if self.pokemon2.hp == 0:
            dead_pokemon_name2 = self.pokemon2.name
            del self.pokemon_team2[self.current_pokemon2]
            self.cpu_switch_pokemon()
            print("\n" + "The CPUs'" + dead_pokemon_name2 + "had died! They switched to " + self.pokemon2.name)

      #check for team
         if len(self.pokemon_team2) == 0:
            self.game_over = True

   def check_win(self):
      #if cpu won
      if len(self.pokemon_team) == 0:
         print("\n" + "Game Over! You Lost in " + self.round_counter + " rounds.")
      #if user won
      elif len(self.pokemon_team2) == 0:
         print("\n" + "Game Over! You Won in " + self.round_counter + " rounds.")

game = Battle()
game.interface() 