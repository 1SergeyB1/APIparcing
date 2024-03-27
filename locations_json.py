from requests import get
from json import dump

response = get("https://rickandmortyapi.com/api/location").json()
name = 1
while response['info']['next']:
    print(response)
    with open(f'locations_json/{name}.json', 'w') as file:
        dump(response, file)
    response = get(response['info']['next']).json()
    name += 1
print(response)
with open(f'locations_json/{name}.json', 'w') as file:
    dump(response, file)
