from api.models.user import User
from api.Repositories.db import DataBase
from datetime import datetime, timedelta
from mongoengine.queryset.visitor import Q


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
    def get_users_with_last_connection(frm, to):
        # Possible values:
        #  1) frm: 5 to: 0  means for the first five days
        #  2) frm: 59 to: 7  after a week until two months
        #  3) frm: -1 to: 60  two months ago or more
        if not frm and to:
            return []
        today = datetime.now().date()
        to_date = today - timedelta(to)
        if frm == -1:
            return User.objects(last_connection__lte=to_date)
        else:
            from_date = today - timedelta(frm)
            return User.objects(Q(last_connection__lte=to_date) & Q(last_connection__gte=from_date))

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
    def update_last_connection(email):
        User.objects(email=email).update(last_connection=datetime.now().date())
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def delete_user_by_email(email):
        User.objects(email=email).delete()

