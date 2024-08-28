import requests


def get_poke_info(pok):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pok_url = base_url + pok
    return (requests.get(pok_url)).json()


def get_abilities(sheet):
    abilities = sheet["abilities"]
    ability_list = []
    for ability in abilities:
        ability2 = ability["ability"]
        ability_list.append(ability2["name"])
    return ability_list


def get_measures(sheet):
    weight = sheet["weight"]
    height = sheet["height"]
    return [weight, height]


def get_image(sheet):
    return sheet['sprites']['front_default']