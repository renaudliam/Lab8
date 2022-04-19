import requests

def get_poke_info(pokemon):
    print("Getting pokemon information..." " ", end="")
    name = pokemon.lower().strip()
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(name))

    if response.status_code == 200:
        print("Success! You can find the details below!")
        return response.json()

    else:
        print('Connection failed...', response.status_code)

        return 