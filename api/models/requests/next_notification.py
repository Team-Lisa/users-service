from pydantic.main import BaseModel


class NextNotification(BaseModel):
    date: str
    email: str