import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDB

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0

        account_from_db = AccountCrudDB.get_account_by_id(db_session, response.id)

        assert response.id == account_from_db.id, 'У аккаунта нет айди'
        assert account_from_db.balance is not None, 'Поле баланса для созданного аккаунта отсутствует в БД'
