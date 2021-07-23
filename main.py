from typing import List

from client import hellfest_client


def filter_locations(locations):
    filtered_locations = [location for location in locations
                          if is_right_hellfests(location, 'HF1 & HF2')
                          and is_capacity_over(location, 3)
                          and is_not_further_than(location, 4000)
                          and is_right_type(location, ['maison', 'appartement', 'chambre'])]
    return filtered_locations


def is_right_hellfests(location, hellfests: str):
    return location['HF'] == hellfests


def is_capacity_over(location, min_nb_people: int):
    return location['nbPerson'] >= min_nb_people


def is_not_further_than(location, max_distance: int):
    return location['HFDist'] < max_distance


def is_right_type(location, types: List[str]):
    return location['type'] in types


if __name__ == '__main__':
    locations = hellfest_client.locations_all()
    print(filter_locations(locations))
