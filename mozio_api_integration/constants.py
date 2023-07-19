import os
from dotenv import dotenv_values

CONFIG = {
    **dotenv_values('.env'),
    **dotenv_values('.env.secrets'),
    **os.environ,
}

BASE_ENDPOINT = 'https://api-testing.mozio.com'

# Request end-point templates for Mozio API v2
SEARCH_ENDPOINT = '/v2/search/'
GET_SEARCH_ENDPOINT = '/v2/search/{search_id}/poll/'
MAKE_RESERVATION_ENDPOINT = '/v2/reservations/'
GET_RESERVATIONS_ENDPOINT = '/v2/reservations/{search_id}/poll/'
DELETE_RESERVATION_ENDPOINT = '/v2/reservations/{reservation_id}'

DEFAULT_PERIOD_RATE_LIMIT = 1  # It reprensents one minute
RATE_LIMIT_PER_PERIOD = int(CONFIG.get('RATE_LIMIT_PER_PERIOD', 30))
