import requests
import json
new_data = []

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/mewtwo")
print(type(pokemon_req))

data = pokemon_req.json()

pokemon_abilities = json.dumps(data['abilities'])
print(type(pokemon_abilities))


for i in range(0, len(data["abilities"])):
     new_data.append(data["abilities"][i])

with open("mewtwo.json", "w") as jsonfile:
    json.dump(new_data, jsonfile)

print(type(pokemon_req.json()))