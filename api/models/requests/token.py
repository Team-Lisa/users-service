from pydantic.main import BaseModel


class Token(BaseModel):
    expo_token: str