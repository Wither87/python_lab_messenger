from fastapi import APIRouter, Depends, HTTPException, status
from deps import get_db, get_current_user
from schemas.user import User, UserCreate, UserInDB
from crud import user_db


router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/", response_model=UserInDB)
async def get_user(user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Получить пользователя по id """
    _user = user_db.get_user_by_id(session=db, id=user_id)
    if _user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return _user


@router.post("/", response_model=User)
async def create_user(user: UserCreate, db=Depends(get_db)):
    """ Создать пользователя """
    _user = user_db.create_user(session=db, user=user)
    return _user


@router.put("/", response_model=UserInDB)
async def update_user(user: User, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Обновить пользователя по id"""
    _user = user_db.update_user_by_id(session=db, id=user_id, user=user)
    return _user


@router.delete("/", response_model=UserInDB)
async def delete_user(user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Удалить пользователя по id """
    _user = user_db.delete_user_by_id(session=db, id=user_id)
    return _user
