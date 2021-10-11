from api.Repositories.user_repository import UserRepository
from api.models.user import User


def test_add_user_successfully(init):
    result = UserRepository.add_user(User(name = "nick"))
    assert result.name == "nick"

def test_get_user_by_email_successfully(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserRepository.add_user(User(name=name,email=email,expo_token=expo_token))
    result = UserRepository.get_user_by_email(email)
    assert result[0].name == name
    assert result[0].email == email
    assert result[0].expo_token == expo_token


def test_delete_all_users(init):
    UserRepository.delete_all_users()
    result = UserRepository.get_all_users()
    assert result.count() == 0
