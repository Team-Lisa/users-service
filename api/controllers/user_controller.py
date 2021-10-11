from api.Repositories.user_repository import UserRepository
from api.models.user import User
from fastapi import HTTPException
import json


class UserController:

    @staticmethod
    def create(user):
        if not user.expo_token:
            user = User(name = user.name, email = user.email)
        else:
            user = User(name = user.name, email = user.email, expo_token = user.expo_token)
        result = UserRepository.add_user(user)
        return {"user": result.convert_to_json()}


    @staticmethod
    def find_by_email(email):
        result = UserRepository.get_user_by_email(email)
        result = map(lambda user: user.convert_to_json(), list(result))
        return {"user": list(result)}

    @staticmethod
    def update_expo_token(token,email):
        result = UserRepository.update_expo_token(token,email)
        result = map(lambda user: user.convert_to_json(), list(result))
        return {"user": list(result)[0]}

