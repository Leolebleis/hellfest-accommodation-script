from jinja2 import Template
import os

from typing import List, Any, Union

from models import Condition


path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "email.html"))
html_email = f.read()


def render_accommodations(accommodations: List[dict[str, Any]], conditions: list[Condition]) -> str:
    t = Template(html_email)
    formatted_email = t.render(_filter_values(conditions),
                               title="Les locations disponibles...",
                               accommodations=accommodations)

    print("Email formatted and rendered.")
    return formatted_email


def _filter_values(conditions: list[Condition]) -> dict[str, Union[str, list[str]]]:
    result = {
        "HF": "HF1 & HF2",
        "nbPerson": "X",
        "types": ["X"],
        "HFDist": "X"
    }

    for condition in conditions:
        if result.get(condition.key):
            result[condition.key] = condition.operand

    return result
