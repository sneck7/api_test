
import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.user_crud import UserCrudDB as User
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateUser:
    def test_create_user_valid(self, api_manager: ApiManager, db_session: Session):

        create_user_request = CreateUserRequest(username='Max20038', password='Pas!sw0rd', role='ROLE_USER')
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, 'Созданого пользователя не в БД'

    @pytest.mark.parametrize(
        "username, password",
        [
            ('абв', 'Pas!sw0rd'),
            ('ab', 'Pas!sw0rd'),
            ('abv!', 'Pas!sw0rd'),
            ('Maxx1', 'Pas!sw0rdД'),
            ('Maxx2', 'Pas!sw0'),
            ('Maxx3', 'pas!sw0rd'),
            ('Maxx4', 'PAS!SW0RD'),
            ('Maxx5', 'PasSsw0rd'),
            ('Maxx6', 'Pas!swOrd'),
        ]
    )
    def test_create_user_invalid(self, username: str, password: str, api_manager: ApiManager, db_session: Session):

        create_user_request = CreateUserRequest(username=username, password=password, role='ROLE_USER')
        api_manager.admin_steps.create_user_invalid(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, 'Пользователь создан, ошибка'



