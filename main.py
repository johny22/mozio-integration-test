import os
from dotenv import dotenv_values

from mozio_api_integration.api_client import MozioAPIClient
from mozio_api_integration.constants import *


config = {
    **dotenv_values('.env'),
    **dotenv_values('.env.secrets'),
    **os.environ,
}

import pdb
# pdb.set_trace()
API_KEY = config['MOZIO_INTEGRATION_API_KEY']
print(API_KEY)
print(RATE_LIMIT_PER_PERIOD)

client = MozioAPIClient(API_KEY)
response = client.get(
    GET_SEARCH.format(search_id='0d0e136562854492a2c2629b384a40eb')
)
print(response)