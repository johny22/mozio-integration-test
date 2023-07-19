import logging
import time

from .cancel_reservation_use_case import CancelReservationUseCase
from .make_reservation_use_case import MakeReservationUseCase
from .picking_cheapest_vehicle_use_case import PickingCheapestVehicleUseCase
from .check_reservation_use_case import CheckReservationUseCase
from ..constants import CONFIG, ReservationStatus
from ..utils import define_log_level


logging.basicConfig(
    filename='application.log',
    encoding='utf-8',
    level=define_log_level(CONFIG['LOG_LEVEL']),
    format='%(asctime)s %(levelname)s:%(message)s'
)


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
        logging.info('Starting Booking flow...')
        result_id, search_id = self.picking_cheapest_car_use_case.execute(
            **kwargs)
        logging.debug(f'Search with id "{search_id}" was created...')

        reservation_params = {
            'result_id': result_id,
            'search_id': search_id,
            'email': kwargs.get('email'),
            'phone_number': kwargs.get('phone_number'),
            'first_name': kwargs.get('first_name'),
            'last_name': kwargs.get('last_name'),
            'provider_name': kwargs.get('provider_name'),
            'airline': kwargs.get('airline', ''),
            'flight_number': kwargs.get('flight_number', '')
        }
        self.reservation_use_case.execute(
            **reservation_params)

        if reservation_id := self.confirm_reservation(search_id):
            self.cancel_reservation_use_case.execute(reservation_id)
            print('Reservation cancelled successfully!')
        else:
            print('Reservation not found or already cancelled!')
        logging.info('Ending Booking flow...')

    def confirm_reservation(self, search_id):
        logging.info('Trying to confirm reservation...')
        waiting_time = 7
        times_to_try = 5
        status = ''
        reservation_id = ''
        confirmation_number = ''

        for ntry in range(1, times_to_try + 1):
            time.sleep(waiting_time)
            logging.info(f'Confirmation try {ntry}...')

            response = self.check_reservation_use_case.execute(search_id)
            status = response.get('status', ReservationStatus.PENDING.value)
            reservations = response.get('reservations', [])

            if status == ReservationStatus.COMPLETED.value and len(reservations) == 0:
                logging.info(
                    'Confirmation done, although there is no reservations...')
                break
            elif status == ReservationStatus.COMPLETED.value:
                reservation_id = reservations[0]['id']
                confirmation_number = reservations[0]['confirmation_number']
                print('Your reservation was confirmed! The Id is',
                      f'{reservation_id} having "{confirmation_number}"',
                      'as Confirmation Code.')
                break
            else:
                logging.info('It was not possible to confirm!',
                             'Reservation still maybe being processed...')
        return reservation_id
