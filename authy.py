import json

import requests

from utils import read_json

def authenticate():
    # load creds
    creds = read_json('creds', 'petfinder')

    payload = {
        "grant_type": "client_credentials",
        "client_id": creds['client_id'],
        "client_secret": creds['client_secret']
    }

    url = f'https://api.petfinder.com/v2/oauth2/token'

    res = requests.post(url, data=payload)
    res_json = json.loads(res.text)

    token = res_json['access_token']

    header = {
        "Authorization": f'Bearer {token}'
    }

    return header
