import requests 
import csv 

url = "https://pokeapi.co/api/v2/pokemon/"

#iterate through 1126 pokemon 

def query(id):
    #establishes payload
    url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    # sends payload
    response = requests.get(url) 
    return response.json()

x = 1
results = query(x)

pokemon_moves = {}
while x < 1127:
    results = query(x)
    name = results["name"]
    move_list = []
    for move in results["moves"]:
        move = move["move"]["name"]
        move_list.append(move)
    pokemon_moves[name] = move_list
    x += 1
print(pokemon_moves)
