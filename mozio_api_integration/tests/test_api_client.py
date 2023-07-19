import pytest

from ..api_client import MozioAPIClient
from ..constants import CONFIG, GET_SEARCH_ENDPOINT
from ..use_cases.picking_cheapest_vehicle_use_case import PickingCheapestVehicleUseCase


@pytest.fixture
def api_client():
    api_key = CONFIG['MOZIO_INTEGRATION_API_KEY']
    return MozioAPIClient(api_key)


@pytest.fixture
def search_cheapest_car_sfo():
    request_params = {
        'provider_name': 'Dummy External Provider',
        'start_address': '44 Tehama Street, San Francisco, CA, USA',
        'end_address': 'SFO',
        'mode': 'one_way',
        'pickup_datetime': '2023-12-01 15:30',
        'num_passengers': 2,
        'currency': 'USD',
        'campaign': 'JONES ROMÃO BEZERRA',
        'email': 'mailtest003@gmail.com',
        'phone_number': '+5517999999997',
        'first_name': 'Guido',
        'last_name': 'Rossum',
        'airline': 'AA',
        'flight_number': '123'
    }
    use_case = PickingCheapestVehicleUseCase()
    return use_case.execute(**request_params)


@pytest.fixture
def api_key():
    return CONFIG['MOZIO_INTEGRATION_API_KEY']


@pytest.fixture
def api_client_wrong_api_key():
    api_key = 'Hey!'
    return MozioAPIClient(api_key)


def test_get_auth_headers(api_client, api_key):
    headers = api_client.get_auth_headers()
    assert headers == {'Api-Key': api_key}


def test_get_auth_headers_wrong_api_key(api_client_wrong_api_key, api_key):
    headers = api_client_wrong_api_key.get_auth_headers()
    assert headers != {'Api-Key': api_key}


def test_get(api_client, search_cheapest_car_sfo):
    _, search_id = search_cheapest_car_sfo
    response = api_client.get(GET_SEARCH_ENDPOINT.format(search_id=search_id))
    assert set(['results', 'more_coming']).issubset(set(response))
