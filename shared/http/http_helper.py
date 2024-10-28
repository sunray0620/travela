'''
This module sends http requests.
'''

from typing import Dict, Optional
import requests

DEFAULT_TIMEOUT = 60

def send_http_request(
    url: str,
    method: str = 'GET',
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, str]] = None,
    json: Optional[Dict] = None,
) -> requests.Response:
    '''Send a POST http request, and return response.'''
    try:
        response = requests.request(
            method=method,
            url=url,
            data=data,
            json=json,
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )
        response.raise_for_status()  # Raise an HTTPError if the response status code is 4xx/5xx
        return response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        raise
