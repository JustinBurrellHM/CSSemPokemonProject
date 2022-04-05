from random import randint


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
  
  def __init__(self, stats, moves):
    self.name = stats["name"]
    self.hp = stats["baseStats"]["hp"]
    self.atk = stats["baseStats"]["atk"]
    self.defe = stats["baseStats"]["def"]
    self.spa = stats["baseStats"]["spa"]
    self.spd = stats["baseStats"]["spd"]
    self.spe = stats["baseStats"]["spe"]
    self.type = [stats["types"]]
    self.moves = moves
  
  # move function
  def move(self, move, p2):
    damage = self.take_damage(p2, move)
    p2.hp = p2.hp - damage

  # #take_damage functionacs
  def take_damage(self, p2, move):

    #critical hit
    x = randint(1, 25)
    if x == 24:
      crit = 1.5
    else:
      crit = 1

    #random factor
    y = randint(85,101)
    random = y/100


    damage = (((move.basepower*(self.atk/p2.defe))/50)+2)*crit*random
    return damage

  # #heal function

    