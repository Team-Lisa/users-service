import pytest

from api.controllers.user_controller import UserController
from api.models.requests.user import User
from fastapi import HTTPException


def test_response(init):
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


