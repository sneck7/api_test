import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDB

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.fixtures.user_fixture import credit_user_request, credit_account_response



@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self, db_session: Session,
                            api_manager: ApiManager,
                            credit_user_request,
                            credit_account_response):

        credit_get_response = api_manager.user_steps.credit_get_valid(
            credit_user_request,
            credit_account_response.id,
            amount=7000,
            term_months=12
        )
        assert credit_get_response.balance == 7000

        credit_from_db = CreditCrudDB.get_credit_by_account_id(db_session, credit_account_response.id)
        assert credit_from_db.balance is not None, 'Баланс не указан'
        assert credit_from_db.term_months == 12




    @pytest.mark.parametrize(
        'amount',
        [4999, 15001]
    )
    def test_credit_request_invalid(self, db_session, api_manager, credit_user_request, credit_account_response, amount):

        credit_get_response = api_manager.user_steps.credit_get_invalid(
            credit_user_request,
            credit_account_response.id,
            amount=amount,
            term_months=12
        )

        credit_from_db = CreditCrudDB.get_credit_by_account_id(db_session, credit_account_response.id)
        assert credit_from_db is None
        assert credit_account_response.balance == 0
