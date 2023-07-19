import logging

from mozio_api_integration.services.mozio_integration_service import\
    MozioIntegrationService


class MakeReservationUseCase:

    def __init__(self, service=None):
        self.service = service or MozioIntegrationService()

    def execute(self, **kwargs):
        logging.info('Starting reservation...')
        result = self.service.make_reservation(**kwargs)
        logging.info('Reservation done...')
        return result
