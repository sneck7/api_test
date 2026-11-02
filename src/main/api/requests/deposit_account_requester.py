from http import HTTPStatus

import requests

from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.requests.requester import Requester


class DepositAccountRequester(Requester):

    def post(self, deposit_account_request: DepositAccountRequest):
        response = requests.post(
            url=f'{self.base_url}/account/deposit',
            json=deposit_account_request.model_dump(),
            headers=self.headers
        )

        self.response_spec(response)

        if response.status_code == HTTPStatus.BAD_REQUEST:
            return response

        return DepositAccountResponse(**response.json())

