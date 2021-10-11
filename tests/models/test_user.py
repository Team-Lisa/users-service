from api.models.user import User


def test_model_to_json():
    name = "mockname"
    email = "mockname@email.com"
    expo_token = "123"
    user = User(name=name,email=email,expo_token=expo_token)
    assert user.convert_to_json() == {
         "name": name,
         "email": email,
         "expo_token": expo_token
    }
