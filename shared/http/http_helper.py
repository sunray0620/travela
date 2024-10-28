import requests
from typing import Dict

def send_http_get_request(url: str, headers: Dict) -> str:
    try:
        response = requests.get(url=url, headers=headers)
        if response.ok:
            return response.text
        else:
            print(f'Failed to get data. Status code: {response.status_code}')
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

def send_http_post_request(url: str, data, json, headers: Dict) -> str:
    try:
        response = requests.post(url, data=data, json=json, headers=headers)
        if response.ok:
            return response.text
        else:
            print(f'Failed to post data. Status code: {response.status_code}')
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
