from mozio_api_integration.services.mozio_integration_service import\
    MozioIntegrationService


class CheckReservationUseCase:

    def __init__(self, service=None):
        self.service = service or MozioIntegrationService()

    def execute(self, search_id):
        return self.service.check_reservation(search_id)
