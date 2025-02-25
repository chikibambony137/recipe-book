from fastapi import APIRouter, HTTPException, status # type: ignore
from app.auth import get_password_hash
from app.schemas import SUserRegister


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    # user = await UsersDAO.find_one_or_none(email=user_data.email)
    # if user:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail='Пользователь уже существует'
    #     )
    # user_dict = user_data.dict()
    # user_dict['password'] = get_password_hash(user_data.password)
    # await UsersDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}