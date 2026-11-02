from dataclasses import dataclass

import pytest

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def account_create_response(create_user_request, api_manager):
    return api_manager.user_steps.create_account(create_user_request)


@dataclass
class PreparedData:
    sender: CreateUserRequest
    sender_account_id: int
    receiver_account_id: int

@pytest.fixture
def transfer_account_data(api_manager):
    user_1 = RandomModelGenerator.generate(CreateUserRequest)
    user_2 = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_1)
    api_manager.admin_steps.create_user(user_2)
    user1_account_response = api_manager.user_steps.create_account(user_1)
    user2_account_response = api_manager.user_steps.create_account(user_2)
    api_manager.user_steps.deposit_account(user_1, user1_account_response.id, 2000)
    return PreparedData(
        sender=user_1,
        sender_account_id=user1_account_response.id,
        receiver_account_id=user2_account_response.id
    )

@pytest.fixture
def credit_user_request(api_manager):
    user = RandomModelGenerator.generate(CreateUserRequest, role='ROLE_CREDIT_SECRET')
    api_manager.admin_steps.create_user(user)
    return user

@pytest.fixture
def credit_account_response(api_manager, credit_user_request):
    return api_manager.user_steps.create_account(credit_user_request)

@pytest.fixture
def credit_get_request(api_manager, credit_user_request, credit_account_response):
    return api_manager.user_steps.credit_get_valid(credit_user_request, credit_account_response.id, amount=7000, term_months=12)