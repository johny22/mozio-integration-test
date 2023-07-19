from ..api_client import MozioAPIClient
from ..constants import *


class MozioIntegrationService:

    def __init__(self, api_client=None):
        self.api_client = api_client or MozioAPIClient(
            CONFIG['MOZIO_INTEGRATION_API_KEY']
        )

    def search(self, **kwargs):
        request_params = {
            **kwargs
        }
        return self.api_client.post(SEARCH_ENDPOINT, request_params)

    def poll_search(self, search_id):
        query_resource = GET_SEARCH_ENDPOINT.format(search_id=search_id)
        return self.api_client.get(query_resource)

    def get_available_voyages(self, search_id):
        results = []
        fetch_more = True
        while fetch_more:
            response = self.poll_search(search_id)
            results += response.get('results', [])
            fetch_more = response.get('more_coming')
        return results

    def make_reservation(self, **kwargs):
        request_params = {
            **kwargs,
            'provider': {'name': kwargs.get('provider_name')}
        }
        return self.api_client.post(MAKE_RESERVATION_ENDPOINT, request_params)

    def check_reservation(self, search_id):
        query_resource = GET_RESERVATIONS_ENDPOINT.format(search_id=search_id)
        return self.api_client.get(query_resource)

    def cancel_reservation(self, reservation_id):
        method_url = DELETE_RESERVATION_ENDPOINT.format(
            reservation_id=reservation_id)
        return self.api_client.delete(method_url)
