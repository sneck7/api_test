import pytest

from src.main.api.db.crud.account_crud import AccountCrudDB
from src.main.api.fixtures.api_fixture import api_manager



@pytest.mark.api
class TestTransferAccount:

    def test_transfer_account(self, api_manager, transfer_account_data, db_session):
        account_transfer_response = api_manager.user_steps.transfer_account_valid(
            transfer_account_data.sender,
            transfer_account_data.sender_account_id,
            transfer_account_data.receiver_account_id,
            amount=767)

        assert account_transfer_response.fromAccountIdBalance == 1233

        assert AccountCrudDB.get_account_by_id(db_session, transfer_account_data.sender_account_id).balance == 1233
        assert AccountCrudDB.get_account_by_id(db_session, transfer_account_data.receiver_account_id).balance == 767


    @pytest.mark.parametrize(
        'amount',
        [499, 10001]
    )
    def test_transfer_account_invalid(self, api_manager, transfer_account_data, amount, db_session):
        account_transfer_response = api_manager.user_steps.transfer_account_invalid(
            transfer_account_data.sender,
            transfer_account_data.sender_account_id,
            transfer_account_data.receiver_account_id,
            amount=amount)

        assert AccountCrudDB.get_account_by_id(db_session, transfer_account_data.sender_account_id).balance == 2000
        assert AccountCrudDB.get_account_by_id(db_session, transfer_account_data.receiver_account_id).balance == 0


