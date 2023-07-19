from mozio_api_integration.services.mozio_integration_service import\
    MozioIntegrationService


class MakeReservationUseCase:

    def __init__(self, service=None):
        self.service = service or MozioIntegrationService()

    def execute(self, **kwargs):
        return self.service.make_reservation(**kwargs)
