import requests
from ratelimit import limits

from .constants import *


class MozioAPIClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_auth_headers(self):
        return {'Api-Key': self.api_key}

    @limits(calls=RATE_LIMIT_PER_PERIOD, period=DEFAULT_PERIOD_RATE_LIMIT)
    def get(self, query_url):
        try:
            RESOURCE_URL = f'{BASE_ENDPOINT}{query_url}'
            auth_headers = self.get_auth_headers()
            response = requests.get(RESOURCE_URL, headers=auth_headers)
            return response.json()
        except Exception as e:
            raise e
    
    @limits(calls=RATE_LIMIT_PER_PERIOD, period=DEFAULT_PERIOD_RATE_LIMIT)
    def post(self, method_url, payload):
        try:
            RESOURCE_URL = f'{BASE_ENDPOINT}{method_url}'
            auth_headers = self.get_auth_headers()
            response = requests.post(
                RESOURCE_URL,
                headers=auth_headers,
                data=payload
            )
            return response.json()
        except Exception as e:
            raise e
    
    @limits(calls=RATE_LIMIT_PER_PERIOD, period=DEFAULT_PERIOD_RATE_LIMIT)
    def delete(self, method_url):
        try:
            RESOURCE_URL = f'{BASE_ENDPOINT}{method_url}'
            auth_headers = self.get_auth_headers()
            response = requests.delete(RESOURCE_URL, headers=auth_headers)
            return response.json()
        except Exception as e:
            raise e
