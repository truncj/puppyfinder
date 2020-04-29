import datetime
import json
import time

from deepdiff import DeepDiff
import requests

from authy import authenticate
from utils import send_message, rebrandly_maker, read_json

headers = authenticate()
search_url = 'https://api.petfinder.com/v2/animals'

init = read_json('config', 'init')

params = init['params']

count = 0
while 1:
    try:
        print(f'[attempt: {count}] {datetime.datetime.now()}')

        res = requests.request('GET', search_url, headers=headers, params=params)

        if res.status_code != 200:
            print(f'Error on request: {res.status_code} - {res.text}')
            authenticate()
        else:
            results_json = json.loads(res.text)
            animals = results_json['animals']

            if count == 0:
                animals_prev = animals
            else:
                animal_diff = DeepDiff(animals_prev, animals, ignore_order=True)
                animals_prev = animals
                if 'iterable_item_added' in animal_diff:
                    new_animals = animal_diff['iterable_item_added']
                    print(animal_diff)
                    for animal in new_animals:
                        pf_animal = new_animals[animal]
                        pf_url = pf_animal['url']
                        pf_name = pf_animal['name']
                        pf_desc = pf_animal['description']
                        short_url = rebrandly_maker(pf_url)
                        message = f'{pf_desc}\n\nhttps://{short_url}'
                        print(f'*** New Animal Found *** - {pf_name}')
                        send_message(pf_name, message)

            count += 1
            time.sleep(init['timeout'])
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except Exception as e:
        print(f'Exception: {e}')

