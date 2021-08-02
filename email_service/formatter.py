from jinja2 import Template
import os

from typing import List

path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "email.html"))
html_email = f.read()


def render_accommodations(accommodations: List[dict], filters: dict) -> str:
    t = Template(html_email)
    formatted_email = t.render(filters, title="Les locations disponibles...", accommodations=accommodations)
    print(formatted_email)
    return formatted_email
