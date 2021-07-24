import pytest

from filters import is_capacity_over, is_not_further_than, is_right_type, is_right_hellfests

valid_accommodations = [
    {
        "HFDist": 3000,
        "nbPerson": 5,
        "type": "appartement",
        "HF": "HF1 & HF2"
    }, {
        "HFDist": 2000,
        "nbPerson": 4,
        "type": "maison",
        "HF": "HF1 & HF2"
    }, {
        "HFDist": 2000,
        "nbPerson": 6,
        "type": "chambre",
        "HF": "HF1 & HF2"
    }
]


@pytest.mark.parametrize("accommodation", valid_accommodations)
def test_valid_data(accommodation: dict):
    assert is_right_hellfests(accommodation, "HF1 & HF2")
    assert is_capacity_over(accommodation, 3)
    assert is_not_further_than(accommodation, 4000)
    assert is_right_type(accommodation, ["maison", "appartement", "chambre"])


def test_not_right_hellfest():
    assert not is_right_hellfests({"HF": "HF2"}, "HF1 & HF2")


def test_under_capacity():
    assert not is_capacity_over({"nbPerson": 2}, 3)


def test_further_than():
    assert not is_not_further_than({"HFDist": 10000}, 8000)


def test_not_right_type():
    assert not is_right_type({"type": "camping"}, ["maison"])
