class Pokemon:
  def __str__(self):
   return f"Name: {self.name}"
  #  return f"Name: {self.name}, HP: {self.pokemon_hp}, MOVES: {self.moves}"
  
  def __init__(self, stats, moves):
    self.name = stats["name"]
    self.hp = stats["baseStats"]["hp"]
    self.atk = stats["baseStats"]["atk"]
    self.defe = stats["baseStats"]["def"]
    self.spa = stats["baseStats"]["spa"]
    self.spd = stats["baseStats"]["spd"]
    self.spe = stats["baseStats"]["spe"]
    self.moves = [moves]
  
  # move function
  # def move(self, move):
      # user selects a move
      # print(self)
      # returns this move

  # #take_damage function
  def take_damage(self, p1, p2, move):
    damage = (((move["basePower"]*(p1.atk/p2.defe))/50)+2)
  
  # #switch function
  # def switch(self):
  
  # #game_over function
  # def game_over(self):

  # #heal function

    