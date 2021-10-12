from pydantic.main import BaseModel


class Users(BaseModel):
    users: list
