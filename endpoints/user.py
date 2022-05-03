from fastapi import APIRouter
from schemas.user import User, UserInDB
from crud.user import user_database

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/{user_id}")
async def get_user(user_id: int):

    """ Получить пользователя по заданному user_id """
    return user_database[user_id - 1]


@router.post("/", response_model=UserInDB)
async def create_user(user: User):
    """ Создать пользователя """
    user_db = UserInDB(id=len(user_database) + 1, **user.dict())
    return user_db


@router.put("/", response_model=UserInDB)
async def update_user(user_id: int, user: User):
    """ Обновить пользователя """
    user_db = user_database[user_id - 1]
    for param, value in user.dict().items():
        user_db[param] = value

    # Здесь изменения сохраняются в базу
    return user_db


@router.delete("/{user_id}")
def delete_user(user_id: int):
    """ Удалить пользователя по заданному user_id """
    db = list(user_database)
    del db[user_id]
    return db
