import requests as r
import os

URL = 'https://api.github.com/repos/marsvo1ta/POM_SB/dispatches'
BODY = {"event_type": "START"}
HEADERS = {'AUTHORIZATION': f'Bearer {os.environ.get("REMOTE_TOKEN")}',
            'Accept': 'application/vnd.github.everest-preview+json'}

def dispatch():
    response = r.post(URL, json=BODY, headers=HEADERS)
    return response.status_code


