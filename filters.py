from typing import Any

from models import Condition


def filter_accommodations(accommodations: list[dict[str, Any]], conditions: list[Condition]) -> list[dict[str, Any]]:
    """
    Method that runs through all the different filters read from filters.json.
    :param conditions: the filters
    :param accommodations: The unfiltered list of accommodations
    :return: The filtered list of accommodations.
    """
    result = []

    for accommodation in accommodations:
        try:
            if _matches_conditions(accommodation, conditions):
                result.append(accommodation)
        except Exception:
            result.append(accommodation)

    return result


def _matches_conditions(accommodation: dict[str, Any], conditions: list[Condition]) -> bool:
    for condition in conditions:
        if not _matches_condition(accommodation, condition):
            return False

    return True


def _matches_condition(accommodation: dict[str, Any], condition: Condition) -> bool:
    if condition.operator == "=":
        return accommodation.get(condition.key) == condition.operand
    if condition.operator == "IN":
        return accommodation.get(condition.key) in condition.operand
    if condition.operator == "<=":
        return accommodation.get(condition.key) <= condition.operand
    if condition.operator == ">=":
        return accommodation.get(condition.key) >= condition.operand

    return False
