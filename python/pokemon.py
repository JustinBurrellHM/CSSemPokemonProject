import json
from random import randint


class Moves:
  def __repr__(self):
   return f"{self.name}"

  def __init__(self, moves):
    self.name = moves["name"]
    self.accuracy = moves["accuracy"]
    self.basepower = moves["basePower"]
    self.pp = moves["pp"]
    self.type = moves["type"]
    self.priority = moves["priority"]

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
    self.types = None
    self.moves = moves

    with open('/Users/justinburrell/Desktop/HM Comp Sci/Comp Sci Sem/Semester Project/CSSemPokemonProject/json/types.json') as f:
      self.types = json.load(f)
  
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
      print("CRITICAL HIT!!!")
    else:
      crit = 1

    #random factor
    y = randint(85,101)
    random = y/100

    #type effectiveness
    for i in p2.type:
      if move.type == p2.type[i]:
        type_effect = int(self.type[p2.type[i]]["damageTaken"][move.type])
        if type_effect == 0:
          type_effect = 1

    #same type attack bonus
    for i in self.type:
      if self.type[i] == move.type:
        stab = 1.5

    damage = (((move.basepower*(self.atk/p2.defe))/50)+2)*crit*random*stab*type_effect
    return damage
    

    