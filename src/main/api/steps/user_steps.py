from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requsters.crud_requester import CrudRequester
from src.main.api.foundation.requsters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_get_request import CreditGetRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.requests_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):

    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()

        return response

    def deposit_account(self, create_user_request: CreateUserRequest, account_id, amount):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(DepositAccountRequest(accountId=account_id, amount=amount))

        return response

    def deposit_account_invalid(self, create_user_request: CreateUserRequest, account_id, amount):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(DepositAccountRequest(accountId=account_id, amount=amount))

        return response

    def transfer_account_valid(self, create_user_request: CreateUserRequest, from_account_id, to_account_id, amount):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(TransferAccountRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount))

        return response

    def transfer_account_invalid(self, create_user_request: CreateUserRequest, from_account_id, to_account_id, amount):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(TransferAccountRequest(fromAccountId=from_account_id, toAccountId=to_account_id, amount=amount))

        return response

    def credit_get_valid(self, create_user_request: CreateUserRequest, account_id, amount, term_months):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_CREDIT_REQUEST,
            ResponseSpecs.request_created()
        ).post(CreditGetRequest(accountId=account_id, amount=amount, termMonths=term_months))

        return response

    def credit_get_invalid(self, create_user_request: CreateUserRequest, account_id, amount, term_months):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_CREDIT_REQUEST,
            ResponseSpecs.request_bad()
        ).post(CreditGetRequest(accountId=account_id, amount=amount, termMonths=term_months))

        return response

    def credit_repay_valid(self, create_user_request: CreateUserRequest, account_id, credit_id, amount):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=amount))

        return response

    def credit_repay_invalid(self, create_user_request: CreateUserRequest, account_id, credit_id, amount):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.USER_CREDIT_REPAY,
            ResponseSpecs.request_UNPROCESSABLE_ENTITY()
        ).post(CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=amount))

        return response
