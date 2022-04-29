import requests 
import csv 
import pickle

url = "https://pokeapi.co/api/v2/pokemon/"

def query(id):
    #establishes payload
    url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    # sends payload
    response = requests.get(url) 
    return response.json()

x = 1
results = query(x)

pokemon_moves = {}
while x < 899:
    results = query(x)
    name = results["name"]
    move_list = []
    for move in results["moves"]:
        move = move["move"]["name"]
        move_list.append(move)
    pokemon_moves[name] = move_list
    x += 1

#for now, do not include these extra forms because they are referred to different in pokedex.json
# x = 10001
# while x < 10229:
#     results = query(x)
#     name = results["name"]
#     move_list = []
#     for move in results["moves"]:
#         move = move["move"]["name"]
#         move_list.append(move)
#     pokemon_moves[name] = move_list
#     x += 1

#how to pickle an object/dictionary 
pickle_out = open("pokemon_moves.pickle", "wb")
pickle.dump(pokemon_moves, pickle_out)
pickle_out.close()

#how to load and use the pickled object/dictionary
# pickle_in = open("pokemon_moves.pickle", "rb")
# example = pickle.load(pickle_in)
# print(example)