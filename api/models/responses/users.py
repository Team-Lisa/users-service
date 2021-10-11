from pydantic.main import BaseModel


class Users(BaseModel):
    user: list
