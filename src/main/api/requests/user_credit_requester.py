from http import HTTPStatus

import requests
from requests import Response

from src.main.api.models.credit_get_request import CreditGetRequest
from src.main.api.models.credit_get_response import CreditGetResponse
from src.main.api.requests.requester import Requester


class CreditGetRequester(Requester):

    def post(self, credit_get_request: CreditGetRequest) -> CreditGetResponse | Response:

        response = requests.post(
            url=f'{self.base_url}/credit/request',
            json=credit_get_request.model_dump(),
            headers=self.headers
        )

        self.response_spec(response)

        if response.status_code == HTTPStatus.BAD_REQUEST:
            return response

        return CreditGetResponse(**response.json())
