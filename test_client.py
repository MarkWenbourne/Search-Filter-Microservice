import json
import requests

BASE_URL = 'http://127.0.0.1:5003'
items = [
    {'id': 1, 'title': 'CS 361 Sprint Plan', 'category': 'assignment', 'status': 'Not Started'},
    {'id': 2, 'title': 'AAPL Holding', 'category': 'stock', 'status': 'Active'},
    {'id': 3, 'title': 'Living Room Light', 'category': 'device', 'status': 'Offline'},
    {'id': 4, 'title': 'Health Potion', 'category': 'item', 'status': 'Available'}
]

def show(label, resp):
    print(f'=== {label} ===')
    print('Status:', resp.status_code)
    print(json.dumps(resp.json(), indent=2))

search_payload = {'items': items, 'query': 'Light'}
filter_payload = {'items': items, 'filters': {'category': ['assignment', 'device']}}
bad_payload = {'items': 'not-a-list', 'query': 'AAPL'}

show('Search', requests.post(f'{BASE_URL}/search', json=search_payload, timeout=2));
show('Filter', requests.post(f'{BASE_URL}/filter', json=filter_payload, timeout=2));
show('Invalid Request', requests.post(f'{BASE_URL}/search', json=bad_payload, timeout=2));
