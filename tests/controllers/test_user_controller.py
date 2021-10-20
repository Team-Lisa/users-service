import pytest

from api.controllers.user_controller import UserController
from api.models.requests.token import Token
from api.models.requests.user import User
from fastapi import HTTPException


def test_create_user_with_all_parameters(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token
        }
    }

def test_create_user_without_expo_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = ""
    user = User(name=name,email=email,expo_token=expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": None
        }
    }

def test_delete_user_by_email(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    UserController.create(user)
    delete_response = UserController.delete_users(email)
    get_response = UserController.find_by_email("")
    assert delete_response == {"user": "deleted user with specified email"}
    assert len(get_response['users']) == 0

def test_delete_all_users(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    UserController.create(user)
    name = "mockname2"
    email = "mockname@email.com2"
    expo_token = "1234"
    user = User(name=name,email=email,expo_token=expo_token)
    UserController.create(user)
    delete_response = UserController.delete_users("")
    get_response = UserController.find_by_email("")
    assert delete_response == {'users': 'deleted all users'}
    assert len(get_response['users']) == 0

def test_find_user_by_email(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    UserController.create(user)
    response = UserController.find_by_email(email)
    assert response == {
        "users": [
            {
                "name": name,
                "email": email,
                "expo_token": expo_token
            }
        ]
    }

def test_find_all_users(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    UserController.create(User(name=name,email=email,expo_token=expo_token))
    name2 = "mockname2"
    email2 = "mockname2@email.com"
    expo_token2 = "1234"
    UserController.create(User(name=name2,email=email2,expo_token=expo_token2))
    response = UserController.find_by_email("")
    assert len(response["users"]) == 2
    assert response == {
        "users": [
            {
                "name": name,
                "email": email,
                "expo_token": expo_token
            },
            {
                "name": name2,
                "email": email2,
                "expo_token": expo_token2
            }
        ]
    }


def test_update_token(init):
    name = "mockname"
    email = "mockname@email.com"
    empty_expo_token = ""
    user = User(name=name,email=email,expo_token =empty_expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": None
        }
    }
    expo_token = "123"
    response_update = UserController.update_expo_token(expo_token,email)
    assert response_update == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token
        }
    }

def test_post_sessions_existing_user_diferent_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token =expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token
        }
    }
    new_expo_token = "1234"
    user_differen_token = User(name=name,email=email,expo_token =new_expo_token)
    response_sessions = UserController.post_sessions(user_differen_token)
    assert response_sessions == {"message": "session created"}

def test_post_sessions_existing_user_diferent_same_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token =expo_token)
    response = UserController.create(user)
    assert response == response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token
        }
    }
    response_sessions = UserController.post_sessions(user)
    assert response_sessions == {
        "message": "session created"
    }

    response_all_users = UserController.find_by_email("")
    assert len(response_all_users["users"])== 1

def test_post_sessions_non_existing_user_creates_user(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token =expo_token)
    response = UserController.post_sessions(user)
    assert response == {
        "message": "session created"
    }

    response_all_users = UserController.find_by_email("")
    assert len(response_all_users["users"])== 1