from mozio_api_integration.services.mozio_integration_service import\
    MozioIntegrationService


class CancelReservationUseCase:

    def __init__(self, service=None):
        self.service = service or MozioIntegrationService()

    def execute(self, reservation_id):
        return self.service.cancel_reservation(reservation_id)
