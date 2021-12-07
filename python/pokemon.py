class Moves:
  def __repr__(self):
   return f"{self.name}"

  def __init__(self, moves):
    self.name = moves["name"]
    self.accuracy = moves["accuracy"]
    self.basepower = moves["basePower"]
    self.pp = moves["pp"]

class Pokemon:
  def __repr__(self):
   return f"{self.name}"
  #  return f"Name: {self.name}, HP: {self.pokemon_hp}, MOVES: {self.moves}"
  
  def __init__(self, stats, moves):
    self.name = stats["name"]
    self.hp = stats["baseStats"]["hp"]
    self.atk = stats["baseStats"]["atk"]
    self.defe = stats["baseStats"]["def"]
    self.spa = stats["baseStats"]["spa"]
    self.spd = stats["baseStats"]["spd"]
    self.spe = stats["baseStats"]["spe"]
    self.moves = moves
  
  # move function
  def move(self, move, p2):
    damage = self.take_damage(p2, move)
    p2.hp = p2.hp - damage

  # #take_damage function
  def take_damage(self, p2, move):
    damage = (((move["basePower"]*(self.atk/p2.defe))/50)+2)
    return damage

  # #heal function

    