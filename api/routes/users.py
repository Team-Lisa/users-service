from fastapi import APIRouter

from api.models.requests.user import User
from api.controllers.user_controller import UserController
from api.models.responses.message import Message
from api.models.responses.user import User as UserResponse
from api.models.responses.users import Users as UsersResponse
from api.models.requests.token import Token


router = APIRouter(tags=["Users"])


@router.post("/users", response_model=UserResponse)
async def create_user(user: User):
    return UserController.create(user)

@router.get("/users",response_model=UsersResponse)
async def find_user(email: str = ""):
    return UserController.find_by_email(email)

@router.patch("/users", response_model=UserResponse)
async def update_expo_token(token: Token, email: str = ""):
    return UserController.update_expo_token(token.expo_token, email)

@router.patch("/users/nextNotification", response_model=UserResponse)
async def update_next_notification(next_notification_date: str = "", email: str = ""):
    return UserController.update_next_notification(next_notification_date, email)

@router.delete("/users")
async def delete_users(email: str = ""):
    return UserController.delete_users(email)

@router.post("/users/sessions", status_code=201, response_model=Message)
async def post_sesions(user: User):
    return UserController.post_sessions(user)

@router.get("/users/lastConnection")
async def get_users_with_last_connection(frm: int = 0, to: int = 0):
    return UserController.get_users_with_last_connection(frm, to)
