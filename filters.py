from typing import List

import os
import json

path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "filters.json"))
filter_values = json.load(f)


def filter_accommodations(accommodations: List[dict]) -> List[dict]:
    return [accommodation for accommodation in accommodations
            if is_right_hellfests(accommodation, filter_values['HF'])
            and is_capacity_over(accommodation, filter_values['nbPerson'])
            and is_not_further_than(accommodation, filter_values['HFDist'])
            and is_right_type(accommodation, filter_values['types'])]


def is_right_hellfests(accommodation: dict, hellfests: str) -> bool:
    """
    Returns true if the accommodation is for the right type of Hellfest.
    :param accommodation: the accommodation object fetched from hebergement-hellfest.fr
    :param hellfests: the desired hellfest type, e.g. 'HF1 & HF2'
    :return: True if the accommodation is of the right type, otherwise False.
    """
    return accommodation['HF'] == hellfests


def is_capacity_over(accommodation: dict, min_nb_people: int) -> bool:
    """
    Returns true if the accommodation is for at least the number of people specified.
    :param accommodation: the accommodation object fetched from hebergement-hellfest.fr
    :param min_nb_people: the minimum number of people desired
    :return: True if the accommodation is for at least the number of people specified, otherwise False.
    """
    return accommodation['nbPerson'] >= min_nb_people


def is_not_further_than(accommodation: dict, max_distance: int) -> bool:
    """
    Returns true if the accommodation is no further than the distance specified.
    :param accommodation: the accommodation object fetched from hebergement-hellfest.fr
    :param max_distance: the maximum distance from the festival desired
    :return: True if the accommodation is no further than the distance specified, otherwise False.
    """
    return accommodation['HFDist'] < max_distance


def is_right_type(accommodation: dict, types: List[str]) -> bool:
    """
    Returns true if the accommodation is of the right type.
    :param accommodation: the accommodation object fetched from hebergement-hellfest.fr
    :param types: a list of all the types accepted, e.g. ['camping', 'maison']
    :return: True if the accommodation is of one of the types specified, otherwise False.
    """
    return accommodation['type'] in types
