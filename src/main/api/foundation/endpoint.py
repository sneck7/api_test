from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_get_request import CreditGetRequest
from src.main.api.models.credit_get_response import CreditGetResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.transfer_account_response import TransferAccountResponse
from src.main.api.requests.create_account_requster import CreateAccountRequester


@dataclass
class EndPointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndPointConfiguration(
        url='/admin/create',
        request_model=CreateUserRequest,
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndPointConfiguration(
        url='/admin/users',
        request_model=None,
        response_model=None
    )

    LOGIN_USER = EndPointConfiguration(
        url='/auth/token/login',
        request_model=LoginUserRequest,
        response_model=LoginUserResponse
    )

    USER_CREATE_ACCOUNT = EndPointConfiguration(
        url='/account/create',
        request_model=None,
        response_model=CreateAccountResponse
    )

    USER_DEPOSIT_ACCOUNT = EndPointConfiguration(
        url='/account/deposit',
        request_model=DepositAccountRequest,
        response_model=DepositAccountResponse
    )

    USER_TRANSFER_ACCOUNT = EndPointConfiguration(
        url='/account/transfer',
        request_model=TransferAccountRequest,
        response_model=TransferAccountResponse
    )

    USER_CREDIT_REQUEST = EndPointConfiguration(
        url='/credit/request',
        request_model=CreditGetRequest,
        response_model=CreditGetResponse
    )

    USER_CREDIT_REPAY = EndPointConfiguration(
        url='/credit/repay',
        request_model=CreditRepayRequest,
        response_model=CreditRepayResponse
    )