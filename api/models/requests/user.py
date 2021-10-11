from pydantic.main import BaseModel


class User(BaseModel):
    name: str
    email: str
    expo_token: str
