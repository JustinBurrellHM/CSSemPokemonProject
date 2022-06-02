import json
import os
import random
# from msilib import change_sequence
from random import randint

from dotenv import load_dotenv

from option import Option

load_dotenv()


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

  # def get_secondary(self, move):
  #   effect = None
  #   stat = None
  #   stat_number = None
  #   boosts = []
  #   #if the move affects target
  #   #if the move affects user
  #   #if status move 
  #   if move["category"] == "Status":
  #     # if it does stuff to yourself
  #     if move["target"] == "self":
  #       if "boosts" in move:
  #         for stat in move["boosts"]:
  #           stat_number = move["boosts"][stat]
  #           boost = [stat, stat_number]
  #           boosts.append(boost)
  #     if "boosts" in move:
  #       for stat in move["boosts"]:
  #         stat_number = move["boosts"][stat]
  #         boost = [stat, stat_number]
  #         boosts.append(boost)
  #     elif "status" in move:
  #       effect = move["status"]
  #   else:
  #     if does stuff to yourself
  #     if lower opponenet stats 
  #     effect_secondary = move["secondary"]
  #     chance_effect = random.randint(0, 100)
  #     if chance_effect <= int(effect_secondary["chance"]):
  #       effect = effect_secondary["status"]
  #     else:
  #       effect = None
  #   return Option({"move_type": "Secondary", "boosts": boosts, "effects": effect})
    '''
    brn: burn
    par: paralyzed
    frz: frozen
    tox: poisioned
    psn: poisioned
    slp: asleep

    volatileStatus
    confusion
    flinch
    '''

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
    self.status_condition = []

    with open(os.getenv('types')) as f:
      self.types = json.load(f)
  
  # move function
  def move(self, move, p2):
    # effect = self.set_secondary(move)
    # p2.status_condition = effect
    damage = self.set_damage(p2, move)
    p2.hp = p2.hp - damage 
    # accuracy_marker = random.randint(1,101)
    # if accuracy_marker <= move["accuracy"]:
    #   p2.hp = p2.hp - damage
    # else:
    #   print(move + "failed.")

  # #take_damage functionacs
  def set_damage(self, p2, move):
    #critical hit
    x = randint(1, 25)
    if x == 24:
      crit = 1.5
      print("WOW!! A CRITICAL HIT!!!")
    else:
      crit = 1

    #random factor
    y = randint(85,101)
    random = y/100

    #type effectiveness
    type_list = p2.type[0]
    for i in range(len(type_list)):

      type_effect = self.types[type_list[i]]["damageTaken"][move.type]
      if type_effect == 0:
        type_effect = 1

    #same type attack bonus
    type_range = self.type[0]
    stab = 1
    for i in range(len(type_range)):
      if type_range[i] == move.type:
        stab = 1.5

    damage = (((move.basepower*(self.atk/p2.defe))/50)+2)*crit*random*stab*type_effect
    # damage = 100000000000000000000
    return damage

  # def set_secondary(self, option):