from typing import List

from client import hellfest_client


def filter_locations(locations: List[dict]) -> List[dict]:
    return [location for location in locations
            if is_right_hellfests(location, 'HF1 & HF2')
            and is_capacity_over(location, 3)
            and is_not_further_than(location, 4000)
            and is_right_type(location, ['maison', 'appartement', 'chambre'])]


def is_right_hellfests(location: dict, hellfests: str) -> bool:
    """
    Returns true if the location is for the right type of Hellfest.
    :param location: the location object fetched from hebergement-hellfest.fr
    :param hellfests: the desired hellfest type, e.g. 'HF1 & HF2'
    :return: True if the location is of the right type, otherwise False.
    """
    return location['HF'] == hellfests


def is_capacity_over(location: dict, min_nb_people: int) -> bool:
    """
    Returns true if the location is for at least the number of people specified.
    :param location: the location object fetched from hebergement-hellfest.fr
    :param min_nb_people: the minimum number of people desired
    :return: True if the location is for at least the number of people specified, otherwise False.
    """
    return location['nbPerson'] >= min_nb_people


def is_not_further_than(location: dict, max_distance: int) -> bool:
    """
    Returns true if the location is no further than the distance specified.
    :param location: the location object fetched from hebergement-hellfest.fr
    :param max_distance: the maximum distance from the festival desired
    :return: True if the location is no further than the distance specified, otherwise False.
    """
    return location['HFDist'] < max_distance


def is_right_type(location: dict, types: List[str]) -> bool:
    """
    Returns true if the location is of the right type.
    :param location: the location object fetched from hebergement-hellfest.fr
    :param types: a list of all the typees accepted, e.g. ['camping', 'maison']
    :return: True if the location is of one of the types specified, otherwise False.
    """
    return location['type'] in types


if __name__ == '__main__':
    filtered_locations = hellfest_client.locations_all()
    print(filter_locations(filtered_locations))
