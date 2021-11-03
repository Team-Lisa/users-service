from datetime import datetime, timedelta

from api.Repositories.user_repository import UserRepository
from api.models.user import User


def test_add_user_with_all_params_successfully(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    result = UserRepository.add_user(User(name = name,email=email,expo_token=expo_token))
    assert result.name == name
    assert result.email == email
    assert result.expo_token == expo_token

def test_add_user_without_expo_token_successfully(init):
    name = "mockname"
    email = "mockname@email.com"
    result = UserRepository.add_user(User(name = name,email=email))
    assert result.name == name
    assert result.email == email
    assert result.expo_token == None

def test_get_user_by_email_successfully(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserRepository.add_user(User(name=name,email=email,expo_token=expo_token))
    result = UserRepository.get_user_by_email(email)
    assert result[0].name == name
    assert result[0].email == email
    assert result[0].expo_token == expo_token

def test_get_all_users(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserRepository.add_user(User(name=name,email=email,expo_token=expo_token))
    name2 = "mockname2"
    email2 = "mockname2@email.com"
    expo_token2 = "1234"
    UserRepository.add_user(User(name=name2,email=email2,expo_token=expo_token2))
    result = UserRepository.get_user_by_email("")
    assert len(result) == 2
    assert result[0].name == name
    assert result[0].email == email
    assert result[0].expo_token == expo_token
    assert result[1].name == name2
    assert result[1].email == email2
    assert result[1].expo_token == expo_token2

def test_get_users_with_last_connection(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserRepository.add_user(User(name=name,email=email,expo_token=expo_token))
    result = UserRepository.get_users_with_last_connection(5,0)
    assert result.get().name == name
    assert result.get().email == email
    assert result.get().expo_token == expo_token

def test_delete_all_users(init):
    UserRepository.delete_all_users()
    result = UserRepository.get_all_users()
    assert result.count() == 0

def test_delete_user_by_email(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserRepository.add_user(User(name=name,email=email,expo_token=expo_token))
    UserRepository.delete_user_by_email(email)
    result = UserRepository.get_all_users()
    assert result.count() == 0

def test_update_next_notification(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    next_notification = (datetime.now().date() + timedelta(days=1))
    result = UserRepository.add_user(User(name = name,email=email,expo_token=expo_token))
    assert result.name == name
    assert result.email == email
    assert result.expo_token == expo_token
    assert result.next_notification == next_notification
    next_notification = (datetime.now().date() + timedelta(days=2)).strftime('%Y-%m-%d')
    result_update = UserRepository.update_next_notification(next_notification, email=email)
    result_user = result_update[0].convert_to_json()
    assert result_user['name'] == name
    assert result_user['email'] == email
    assert result_user['next_notification'] == next_notification
