import time

from .cancel_reservation_use_case import CancelReservationUseCase
from .make_reservation_use_case import MakeReservationUseCase
from .picking_cheapest_vehicle_use_case import PickingCheapestVehicleUseCase
from .check_reservation_use_case import CheckReservationUseCase


class MozioBookingFlowUseCase:

    def __init__(self, reservation_use_case=None,
                 picking_cheapest_car_use_case=None,
                 cancel_reservation_use_case=None,
                 check_reservation_use_case=None):
        self.reservation_use_case = reservation_use_case or\
            MakeReservationUseCase()
        self.picking_cheapest_car_use_case = picking_cheapest_car_use_case or\
            PickingCheapestVehicleUseCase()
        self.cancel_reservation_use_case = cancel_reservation_use_case or\
            CancelReservationUseCase()
        self.check_reservation_use_case = check_reservation_use_case or\
            CheckReservationUseCase()

    def execute(self, **kwargs):
        result_id, search_id = self.picking_cheapest_car_use_case.execute(
            **kwargs)
        reservation_params = {
            'result_id': result_id,
            'search_id': search_id,
            'email': kwargs.get('email'),
            'phone_number': kwargs.get('phone_number'),
            'first_name': kwargs.get('first_name'),
            'last_name': kwargs.get('last_name'),
            'provider_name': kwargs.get('provider_name'),
            # These two fields above will be present conditionally following the API Doc #Fixme!
            'airline': kwargs.get('airline'),
            'flight_number': kwargs.get('flight_number')
        }
        reservations_response = self.reservation_use_case.execute(
            **reservation_params)

        if reservation_id := self.confirm_reservation(search_id):
            result = self.cancel_reservation_use_case.execute(reservation_id)
            print(result)

    def confirm_reservation(self, search_id):
        waiting_time = 7
        times_to_try = 5
        status = ''
        reservation_id = ''
        for i in range(times_to_try):
            time.sleep(waiting_time)
            response = self.check_reservation_use_case.execute(search_id)
            status = response.get('status', 'pending')
            reservations = response.get('reservations', [])
            if status == 'completed' and len(reservations) == 0:
                break
            elif status == 'completed':
                reservation_id = reservations[0]['id']
                print('Your reservation was confirmed! The id is' +
                      f'{reservation_id}')
                break
        return reservation_id
