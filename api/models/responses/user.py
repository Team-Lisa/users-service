from pydantic.main import BaseModel


class User(BaseModel):
    user: dict
