import json
import os

from client import hellfest_client
from client.email_client import send_email
from email_service import formatter
from filters import filter_accommodations

# We load the filters from filters.json
path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "filters.json"))
filter_values = json.load(f)

if __name__ == '__main__':
    unfiltered_accommodations = hellfest_client.accommodations_all()
    filtered_accommodations = filter_accommodations(unfiltered_accommodations, filter_values)
    print(filtered_accommodations)
    formatted_email = formatter.render_accommodations(filtered_accommodations, filter_values)

    send_email(formatted_email, "Hellfest 2022 - Tous les appartements disponibles :)")

