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
    def update_next_notification(date, email):
        result = UserRepository.update_next_notification(date, email)
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
            UserRepository.update_last_connection(user.email)
            if result["users"][0]["expo_token"] != user.expo_token:
                UserController.update_expo_token(user.expo_token,user.email)
        else:
            UserController.create(user)
        return {"message": "session created"}

    @staticmethod
    def get_users_with_last_connection(frm, to):
        result = UserRepository.get_users_with_last_connection(frm, to)
        result = map(lambda user: user.convert_to_json(), list(result))
        result_list = list(result)
        if len(result_list) == 0:
            return {"users": []}
        return {"users": result_list}
