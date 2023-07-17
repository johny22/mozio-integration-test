import os
from dotenv import load_dotenv


load_dotenv()

BASE_ENDPOINT = 'https://api-testing.mozio.com'

# Request end-point templates for Mozio API v2
SEARCH = '/v2/search/'
GET_SEARCH = '/v2/search/{search_id}/poll/'
DO_RESERVATION = '/v2/reservations/'
GET_RESERVATIONS = '/v2/reservations/{search_id}/poll/'
DELETE_RESERVATION = '/v2/reservations/{confirmation_number}'

DEFAULT_PERIOD_RATE_LIMIT = 1 # It reprensents one minute
RATE_LIMIT_PER_PERIOD = int(os.getenv('RATE_LIMIT_PER_PERIOD', 30))
