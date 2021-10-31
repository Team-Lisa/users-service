from pydantic.main import BaseModel


class User(BaseModel):
    name: str
    email: str
    expo_token: str
    last_connection: str

class CreateUser(BaseModel):
    name: str
    email: str
    expo_token: str