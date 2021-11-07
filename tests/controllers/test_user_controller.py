import pytest

from api.controllers.user_controller import UserController
from api.models.requests.token import Token
from api.models.requests.user import User
from fastapi import HTTPException
from datetime import datetime, timedelta


def test_create_user_with_all_parameters(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    last_connection = datetime.now().date()
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token, last_connection=last_connection, next_notification=next_notification)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token,
            "last_connection": last_connection.isoformat(),
            "next_notification": next_notification
        }
    }

def test_create_user_without_expo_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = ""
    last_connection = datetime.now().date()
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token, last_connection=last_connection, next_notification=next_notification)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": None,
            "last_connection": last_connection.isoformat(),
            "next_notification": next_notification
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
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token, last_connection=last_connection, next_notification=next_notification)
    UserController.create(user)
    response = UserController.find_by_email(email)
    assert response == {
        "users": [
            {
                "name": name,
                "email": email,
                "expo_token": expo_token,
                "last_connection": last_connection,
                "next_notification": next_notification
            }
        ]
    }

def test_find_all_users(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token)
    UserController.create(user)
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
                "expo_token": expo_token,
                "last_connection": last_connection,
                "next_notification": next_notification
            },
            {
                "name": name2,
                "email": email2,
                "expo_token": expo_token2,
                "last_connection": last_connection,
                "next_notification": next_notification
            }
        ]
    }


def test_update_token(init):
    name = "mockname"
    email = "mockname@email.com"
    empty_expo_token = ""
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=empty_expo_token, last_connection=last_connection, next_notification=next_notification)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": None,
            "last_connection": last_connection,
            "next_notification": next_notification
        }
    }
    expo_token = "123"
    response_update = UserController.update_expo_token(expo_token,email)
    assert response_update == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token,
            "last_connection": last_connection,
            "next_notification": next_notification
        }
    }

def test_post_sessions_existing_user_diferent_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token, last_connection=last_connection, next_notification=next_notification)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token,
            "last_connection": last_connection,
            "next_notification": next_notification
        }
    }
    new_expo_token = "1234"
    user_differen_token = User(name=name,email=email,expo_token =new_expo_token, next_notification=next_notification)
    response_sessions = UserController.post_sessions(user_differen_token)
    assert response_sessions == {"message": "session updated"}

def test_post_sessions_existing_user_diferent_same_token(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token, last_connection=last_connection, next_notification=next_notification)
    response = UserController.create(user)
    assert response == response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token,
            "last_connection": last_connection,
            "next_notification": next_notification
        }
    }
    response_sessions = UserController.post_sessions(user)
    assert response_sessions == {
        "message": "session updated"
    }

    response_all_users = UserController.find_by_email("")
    assert len(response_all_users["users"])== 1

def test_post_sessions_non_existing_user_creates_user(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=expo_token,
                next_notification=next_notification)
    response = UserController.post_sessions(user)
    assert response == {
        "message": "session created"
    }

    response_all_users = UserController.find_by_email("")
    assert len(response_all_users["users"])== 1

def test_post_sessions_to_change_last_connection(init):
    name = "mockname"
    email = "mockname@email.com"
    empty_expo_token = ""
    next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    user = User(name=name, email=email, expo_token=empty_expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": None,
            "last_connection": datetime.now().date().strftime('%Y-%m-%d'),
            "next_notification": next_notification
        }
    }
    user = User(name=name, email=email, expo_token=empty_expo_token)
    response_update = UserController.post_sessions(user)
    assert response_update == {
        "message": "session updated"
    }
    response_all_users = UserController.find_by_email("")
    assert response_all_users["users"][0]["last_connection"] == datetime.now().date().strftime('%Y-%m-%d')

def test_get_users_with_last_connection(init):
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "ExpoToken"
    user = User(name=name, email=email, expo_token=expo_token)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name,
            "email": email,
            "expo_token": expo_token,
            "last_connection": datetime.now().date().strftime('%Y-%m-%d'),
            "next_notification": (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
        }
    }
    users = UserController.get_users_with_last_connection(5,0)
    assert users == {
        "users": [
        {
            "name": "mockname",
            "email": "mockname@email.com",
            "expo_token": "ExpoToken",
            "last_connection": datetime.now().date().strftime('%Y-%m-%d'),
            "next_notification": (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
        }
    ]}

    def test_update_next_notification(init):
        name = "mockname"
        email = "mockname@email.com"
        empty_expo_token = ""
        last_connection = datetime.now().date().strftime('%Y-%m-%d')
        next_notification = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
        user = User(name=name, email=email, expo_token=empty_expo_token)
        response = UserController.create(user)
        assert response == {
            "user": {
                "name": name,
                "email": email,
                "expo_token": None,
                "last_connection": last_connection,
                "next_notification": next_notification
            }
        }
        next_notification = (datetime.now().date() + timedelta(days=2)).strftime('%Y-%m-%d')
        response_update = UserController.update_next_notification(next_notification, email)
        assert response_update == {
            "user": {
                "name": name,
                "email": email,
                "expo_token": expo_token,
                "last_connection": last_connection,
                "next_notification": next_notification
            }
        }