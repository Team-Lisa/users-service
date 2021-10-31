from api.models.user import User
from api.Repositories.db import DataBase
from datetime import datetime


class UserRepository():

    @staticmethod
    def add_user(user):
        user.last_connection = datetime.now().date()
        return user.save()

    @staticmethod
    def get_user_by_email(value):
        if not value:
            return UserRepository.get_all_users()
        return User.objects(email=value)

    @staticmethod
    def delete_all_users():
        User.objects().delete()

    @staticmethod
    def get_all_users():
        return User.objects()

    @staticmethod
    def update_expo_token(token,email):
        User.objects(email=email).update(expo_token=token)
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def update_last_connection(last_connection, email):
        datetime_object = datetime.strptime(last_connection, '%Y-%m-%d')
        User.objects(email=email).update(last_connection=datetime_object)
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def delete_user_by_email(email):
        User.objects(email=email).delete()

