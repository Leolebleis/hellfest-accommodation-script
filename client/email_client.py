import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
RECIPIENTS = json.loads(os.getenv("RECIPIENTS"))
URI = os.getenv("EMAIL_CLIENT_URI")


def send_email(html_body: str, subject_line: str) -> None:

    if len(RECIPIENTS) == 0:
        raise NotEnoughRecipientsError

    uri = URI

    for idx, recipient in enumerate(RECIPIENTS):
        if idx == 0:
            uri += f"?recipients={recipient}"
        else:
            uri += f"&recipients={recipient}"

    r = requests.post(uri, data=html_body.encode("UTF-8"), headers={
        "X-API-KEY": API_KEY,
        "Subject-Line": subject_line
    })

    print(f"Email sent, ({r.status_code})")

    r.raise_for_status()


class NotEnoughRecipientsError(Exception):
    ...
