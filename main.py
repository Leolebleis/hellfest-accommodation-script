import json
import logging
import os
from typing import Any

from client import hellfest_client
from client.email_client import send_email
from db import AccommodationDatabase
from email_service import formatter
from filters import filter_accommodations
from config import config
from models import Condition

logger = logging.getLogger(__name__)

# We load the filters from filters.json
path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "filters.json"))
conditions_values = json.load(f)

conditions = [Condition(**condition) for condition in conditions_values]


def _check_unsaved(filtered_accommodations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    db = AccommodationDatabase(**config)
    accommodation_ids = [accommodation.get("_id") for accommodation in filtered_accommodations]

    saved_ids = db.select_rows(tuple(accommodation_ids))
    unsaved_ids = set([saved_id[0] for saved_id in saved_ids]) ^ set(accommodation_ids)

    result = []

    for accommodation in filtered_accommodations:
        if accommodation.get("_id") in unsaved_ids:
            result.append(accommodation)

    return result


def _save_ids(ids: list[str]) -> None:
    db = AccommodationDatabase(**config)
    db.insert_rows(ids)


if __name__ == '__main__':
    unfiltered_accommodations = hellfest_client.accommodations_all()
    filtered_accommodations = filter_accommodations(unfiltered_accommodations, conditions)
    logger.info(f"Filter complete, found {len(filtered_accommodations)} accommodations")

    unsaved_accommodations: list[dict[str, Any]] = _check_unsaved(filtered_accommodations)
    number_of_new_accommodations = len(unsaved_accommodations)

    logger.info(f"Found {number_of_new_accommodations} new accommodations posted.")

    formatted_email = formatter.render_accommodations(unsaved_accommodations, conditions)

    try:
        send_email(formatted_email, f"Hellfest 2022 - {number_of_new_accommodations} nouvelles annonces :)")

        unsaved_ids = [accommodation.get("_id") for accommodation in unsaved_accommodations]

        if len(unsaved_ids) > 0:
            _save_ids(unsaved_ids)
    except Exception as e:
        logger.error("Error while sending email")
        send_email(e.__str__(), "Error sending Hellfest accommodation email :(")
