import pytest

from src.main.api.fixtures.api_fixture import api_manager


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account(self, api_manager, create_user_request, account_create_response):

        account_deposit_response = api_manager.user_steps.deposit_account(
            create_user_request,
            account_create_response.id,
            amount=1000.5
        )
        assert account_deposit_response.balance == 1000.5

    @pytest.mark.parametrize(
        'amount', [999, 9001]
    )
    def test_deposit_account_invalid(self, api_manager, create_user_request, account_create_response, amount):

        api_manager.user_steps.deposit_account_invalid(create_user_request, account_create_response.id, amount)

