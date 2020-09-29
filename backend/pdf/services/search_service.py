import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def search_redfin_autocomplete_api(url):
    response = requests.get(url=url, headers=HEADERS)
    response_json = json.loads(response.content[4:])
    for data in response_json.get('payload').get('sections'):
        if data.get('name') == 'Addresses':
            return {'properties': data.get('rows')}
