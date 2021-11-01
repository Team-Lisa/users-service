from api.models.user import User
from datetime import datetime


def test_model_with_all_parameters_convert_to_json():
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    user = User(name=name,email=email,expo_token=expo_token,last_connection=last_connection)
    assert user.convert_to_json() == {
         "name": name,
         "email": email,
         "expo_token": expo_token,
         "last_connection": last_connection
    }

def test_model_without_expo_token_convert_to_json():
    name = "mockname"
    email = "mockname@email.com"
    expo_token = ""
    last_connection = datetime.now().date().strftime('%Y-%m-%d')
    user = User(name=name,email=email,last_connection=last_connection)
    assert user.convert_to_json() == {
         "name": name,
         "email": email,
         "expo_token": None,
        "last_connection": last_connection
    }
