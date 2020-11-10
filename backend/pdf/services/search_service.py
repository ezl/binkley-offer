import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def search_redfin_autocomplete_api(url):
    response = requests.get(url=url, headers=HEADERS)
    response_json = json.loads(response.content[4:])
    properties = []
    for data in response_json.get('payload').get('sections'):
        if data.get('name') == 'Addresses':
            # To Remove in Future, only temporar for Illinois
            for row in data.get('rows'):
                if row.get('url')[1::].split('/')[0] == 'IL':
                    properties.append(row)
            return {'properties': properties}
