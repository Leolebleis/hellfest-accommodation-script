import requests
import os
import json
from urllib3.exceptions import HTTPError

# We load the API config from hellfest_config.json
path_to_here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(path_to_here, "hellfest_config.json"))
config = json.load(f)


def accommodations_all() -> list[dict]:
    """
    Fetches accommodation data from hellfest-hebergement.fr
    :return: the list of all available accommodations
    """
    body = {'action': 'annonces'}
    r = requests.post(config['URI'], body)
    r.raise_for_status()
    if r.json()['status'] != 'Success':
        http_error_message = u'%s Server Error: %s for url: %s' % (r.status_code, r.json()['message'], r.url)
        raise HTTPError(http_error_message)

    return r.json()['response']
