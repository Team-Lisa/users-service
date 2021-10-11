import pytest
from api.Repositories.user_repository import UserRepository
from api.Repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    UserRepository.delete_all_users()
    return 0
