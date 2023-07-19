from mozio_api_integration.use_cases.mozio_booking_flow_use_case import MozioBookingFlowUseCase


use_case = MozioBookingFlowUseCase()
request_params = {
    'provider_name': 'Dummy External Provider',
    'start_address': '44 Tehama Street, San Francisco, CA, USA',
    'end_address': 'SFO',
    'mode': 'one_way',
    'pickup_datetime': '2023-12-01 15:30',
    'num_passengers': 2,
    'currency': 'USD',
    'campaign': 'JONES ROMÃO BEZERRA',
    'email': 'mailtest002@gmail.com',
    'phone_number': '+5511999999997',
    'first_name': 'Xico',
    'last_name': 'Tripa',
    'airline': 'AA',
    'flight_number': '123'
}
use_case.execute(**request_params)
