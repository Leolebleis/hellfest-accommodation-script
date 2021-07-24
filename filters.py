def filter_accommodations(accommodations: list[dict], filters: list[dict]) -> list[dict]:
    """
    Method that runs through all the different filters read from filters.json.
    :param accommodations: The unfiltered list of accommodations
    :return: The filtered list of accommodations.
    """
    return [accommodation for accommodation in accommodations
            if is_right_hellfests(accommodation, filters['HF'])
            and is_capacity_over(accommodation, filters['nbPerson'])
            and is_not_further_than(accommodation, filters['HFDist'])
            and is_right_type(accommodation, filters['types'])]


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


def is_right_type(accommodation: dict, types: list[str]) -> bool:
    """
    Returns true if the accommodation is of the right type.
    :param accommodation: the accommodation object fetched from hebergement-hellfest.fr
    :param types: a list of all the types accepted, e.g. ['camping', 'maison']
    :return: True if the accommodation is of one of the types specified, otherwise False.
    """
    return accommodation['type'] in types
