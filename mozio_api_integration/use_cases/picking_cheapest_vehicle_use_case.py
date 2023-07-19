import logging
from decimal import Decimal

from mozio_api_integration.services.mozio_integration_service import\
    MozioIntegrationService


class PickingCheapestVehicleUseCase:

    def __init__(self, service=None):
        self.service = service or MozioIntegrationService()

    def execute(self, **kwargs):
        logging.info('Choosing the best vehicle...')
        provider_name = kwargs.get('provider_name')
        search_result = self.service.search(**kwargs)
        search_id = search_result.get('search_id')

        available_voyages = self.service.get_available_voyages(search_id)
        if provider_name:
            available_voyages = self.filter_by_provider_name(
                available_voyages, provider_name
            )
        sorted_ = sorted(
            available_voyages,
            key=lambda x: Decimal(x['total_price']['total_price']['value'])
        )
        logging.info('Vehicle defined...')

        return sorted_[0]['result_id'], search_id

    def filter_by_provider_name(self, result_set, provider_name):
        return list(filter(
            lambda item:
                item['steps'][0]['details']['provider_name'] == provider_name,
            result_set
        ))
