from fastapi import APIRouter

from api.models.requests.token import Token
from api.models.requests.user import User
from api.controllers.user_controller import UserController
from api.models.responses.user import User as UserResponse
from api.models.responses.users import Users as UsersResponse


router = APIRouter(tags=["Users"])


@router.post("/users", response_model=UserResponse)
async def create_user(user: User):
    return UserController.create(user)


@router.get("/users",response_model=UsersResponse)
async def find_user(email: str = ""):
    return UserController.find_by_email(email)

@router.patch("/user", response_model=UserResponse)
async def update_expo_token(email: str, token: Token):
    return UserController.update_expo_token(token,email)
