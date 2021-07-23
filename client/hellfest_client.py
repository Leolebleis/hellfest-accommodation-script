import requests
from urllib3.exceptions import HTTPError

URI = 'https://hellfest-hebergement.fr/api/index.php?newAPI=1'


def locations_all():
    body = {'action': 'annonces'}
    r = requests.post(URI, body)
    r.raise_for_status()
    if r.json()['status'] != 'Success':
        http_error_message = u'%s Server Error: %s for url: %s' % (r.status_code, r.json()['message'], r.url)
        raise HTTPError(http_error_message)

    return r.json()['response']
