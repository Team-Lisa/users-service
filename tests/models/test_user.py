from api.models.user import User


def test_model_with_all_parameters_convert_to_json():
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    assert user.convert_to_json() == {
         "name": name,
         "email": email,
         "expo_token": expo_token
    }

def test_model_without_expo_token_convert_to_json():
    name = "mockname"
    email = "mockname@email.com"
    expo_token = ""
    user = User(name=name,email=email)
    assert user.convert_to_json() == {
         "name": name,
         "email": email,
         "expo_token": None
    }
