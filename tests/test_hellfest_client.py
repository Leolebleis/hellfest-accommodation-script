import pytest

from client.hellfest_client import accommodations_all
from urllib3.exceptions import HTTPError


def test_hellfest_hebergement_client():
    try:
        accommodations_all()
    except HTTPError:
        pytest.fail("Could not fetch accommodations from hellfest-hebergement.fr/")
