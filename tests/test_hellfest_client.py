import pytest

from client.hellfest_client import locations_all
from urllib3.exceptions import HTTPError


def test_hellfest_hebergement_client():
    try:
        locations_all()
    except HTTPError:
        pytest.fail("Could not fetch locations from hellfest-hebergement.fr/")
