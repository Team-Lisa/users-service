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
        return {"users": list(result)}

    @staticmethod
    def update_expo_token(token,email):
        result = UserRepository.update_expo_token(token,email)
        result = map(lambda user: user.convert_to_json(), list(result))
        result_list = list(result)
        if len(result_list) > 0:
            return {"user": result_list[0]}
        return {"user": []}

    @staticmethod
    def delete_users(email):
        if not email:
            UserRepository.delete_all_users()
            return {"users": "deleted all users"}
        else:
            UserRepository.delete_user_by_email(email)
            return {"user": "deleted user with specified email"}

    @staticmethod
    def post_sessions(user):
        result =  UserController.find_by_email(user.email)
        if result["users"]:
            if result["users"][0]["expo_token"] != user.expo_token:
                return UserController.update_expo_token(user.expo_token,user.email)
            return {"user": "expo token matched"}
        else:
            return UserController.create(user)

