class Pokemon:
  def __str__(self):
   return f"Name: {self.name}, HP: {self.pokemon_hp}, MOVES: {self.moves}"
  
  def __init__(self, stats, moves):
    self.name = stats["name"]
    self.pokemon_hp = stats["baseStats"]["hp"]
    self.pokemon_atk = stats["baseStats"]["atk"]
    self.pokemon_def = stats["baseStats"]["def"]
    self.pokemon_spa = stats["baseStats"]["spa"]
    self.pokemon_spd = stats["baseStats"]["spd"]
    self.pokemon_spe = stats["baseStats"]["spe"]
    self.moves = moves
  

    #move function
    # def move(self):
    #     # user selects a move 
    #     # print(self)
    #     # returns this move

    # #take_damage function
    # def take_damage(self, move):
    
    # #switch function
    # def switch(self):
    
    # #game_over function
    # def game_over(self):

    # #heal function

    