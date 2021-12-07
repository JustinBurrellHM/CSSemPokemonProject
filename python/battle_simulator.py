import json
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

      with open('../json/pokedex.json') as f:
         pokedex = json.load(f)

      with open('../json/moves.json') as f:
         moves = json.load(f)

      player1p1 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
      player1p2 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

      player2p1 = Pokemon(pokedex["zaciancrowned"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])
      player2p2 = Pokemon(pokedex["venusaur"], [Moves(moves["quickattack"]), Moves(moves["closecombat"])])

      #automate pokemon_team list so the list can have every pokemon no the team 
      self.pokemon_team = [player1p1, player1p2]

      self.pokemon_team2 = [player2p1, player2p2]

   def interface(self):
      self.current_pokemon = 0
      self.current_pokemon2 = 0
      self.pokemon = self.pokemon_team[self.current_pokemon]
      self.pokemon2 = self.pokemon_team2[self.current_pokemon2]

      while self.game_over == False:
         input("Welcome to the Pokémon Battle Simulator. Press enter to continue ")
         if self.pokemon.spe > self.pokemon2.spe:
            self.user_selection()
         elif self.pokemon2.spe > self.pokemon.spe:
            self.cpu_selection()
      
      self.check_win()

   def print_list(self, l):
      string_pokemon = [str(i) for i in l]
      seperator = ", "
      return seperator.join(string_pokemon)

   #user-based functions
   def user_selection(self):
      selection = input("Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "Would you like to [A]ttack or [S]witch Pokémon? ")

      if selection == "A":
         self.attack_pokemon()

      elif selection == "S":
         self.switch_pokemon()
   
   def attack_pokemon(self):
      move_selection = input("Pick your move:\n" + self.print_list(self.pokemon.moves) + " ")
      self.pokemon.move(move_selection)

   def switch_pokemon(self):
      switch_selection = input("Here is you team:\n" + self.print_list(self.pokemon_team) + "\n" + "You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to. ")
      self.current_pokemon = int(switch_selection) - 1
      self.pokemon = self.pokemon_team[self.current_pokemon]
   
   def check_health(self):
      #check for health
         if self.pokemon.hp == 0:
            del self.pokemon_team[self.current_pokemon]
            dead_pokemon_switch = input("Your " + self.pokemon.name + " has died. You have " + str(len(self.pokemon_team)) + " pokemon avaliable. Pick the pokemon you want to switch to.")
            self.current_pokemon = int(dead_pokemon_switch) - 1
            self.pokemon = self.pokemon_team[self.current_pokemon]

      #check for team
         if len(self.pokemon_team) == 0:
            self.game_over = False
   
   #cpu-based functions
   def cpu_selection(self):
      selection = input("Here is the battle situation: " + self.pokemon.name + " versus " + self.pokemon2.name + ".\n" + "Your " + self.pokemon.name + " has " + str(self.pokemon.hp) + " HP. The opponent's " + self.pokemon2.name + " has " + str(self.pokemon2.hp) + " HP." + "\n" + "The CPU is deciding its move. Click enter to continue. ")

      #percent chances for whether or not cpu attacks or switches
      if selection == "A":
         self.cpu_attack_pokemon()

      elif selection == "S":
         self.cpu_switch_pokemon()
   
   def cpu_attack_pokemon(self):
      cpu_random_move = #random syntax for iterating through moves list
      self.pokemon2.move(cpu_random_move)

   def cpu_switch_pokemon(self):
      cpu_random_switches = #random syntax for iterating through pokemon team and picking an indice value
      self.current_pokemon2 = int(cpu_random_switches) - 1
      self.pokemon2 = self.pokemon_team2[self.current_pokemon2]
   
   def cpu_check_health(self):
      #check for health
         if self.pokemon2.hp == 0:
            del self.pokemon_team2[self.current_pokemon2]
            self.cpu_switch_pokemon()

      #check for team
         if len(self.pokemon_team) == 0:
            self.game_over = False

   def check_win(self):
      #if cpu won
      if len(self.pokemon_team) == 0:
         print("Game Over! You Lose!")
      #if user won
      elif len(self.pokemon_team2) == 0:
         print("Game Over! You Win!")

game = Battle()
game.interface()