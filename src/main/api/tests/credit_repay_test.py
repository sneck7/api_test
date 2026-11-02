import pytest

from src.main.api.db.crud.credit_crud import CreditCrudDB
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.fixtures.user_fixture import credit_user_request


@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(self, api_manager, credit_user_request, credit_get_request, db_session):

        user_repay_response = api_manager.user_steps.credit_repay_valid(
            credit_user_request,
            credit_get_request.id,
            credit_get_request.creditId,
            amount=7000
        )
        assert user_repay_response.amountDeposited == 7000

        credit_from_db = CreditCrudDB.get_credit_by_account_id(db_session, credit_get_request.id)
        assert credit_from_db.balance == 0



    @pytest.mark.parametrize(
        'amount',
        [7001, 6999]
    )
    def test_credit_repay_invalid(self, api_manager, credit_user_request, credit_get_request, amount, db_session):
        user_repay_response = api_manager.user_steps.credit_repay_invalid(
            credit_user_request,
            credit_get_request.id,
            credit_get_request.creditId,
            amount=amount
        )

        credit_from_db = CreditCrudDB.get_credit_by_account_id(db_session, credit_get_request.id)
        assert credit_from_db.balance == -7000

