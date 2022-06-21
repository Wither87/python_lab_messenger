from fastapi import HTTPException, status
from fastapi import APIRouter, Depends
from deps import get_db, get_current_user
from schemas.message import Message
from crud import message_db, chat_db, user_chat_db
from broker.redis import redis

router = APIRouter(
    prefix="/message",
    tags=["message"]
)


def get_user_chat(chat_id:int, user_id:int, db):
    _chat = chat_db.get_chat_by_id(session=db, id=chat_id)
    _user_chat = user_chat_db.get_user_chat_by_ids(session=db, user_id=user_id, chat_id=_chat.id)
    return _user_chat


@router.get("/{message_id}")
def get_message(message_id: int, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Получить сообщение по message_id """
    _message = message_db.get_message_by_id(session=db, id=message_id)
    _user_chat=get_user_chat(chat_id=_message.chat_id, user_id=user_id, db=db)
    if _user_chat is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вас нет в этом чате")

    _message = message_db.set_readed(session=db, message_id=_message.id)
    return _message


@router.post("/")
async def create_message(message: Message, chat_id: int, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Отправка сообщения в чат """
    _user_chat=get_user_chat(chat_id=chat_id, user_id=user_id, db=db)
    if _user_chat is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вас нет в этом чате")

    await redis.publish(f"user-{user_id}", message.text)

    _message = message_db.create_message(session=db, user_id=user_id, chat_id=chat_id, message=message)
    return _message


@router.put("/")
def update_message(message_id: int, message: Message, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Изменение сообщения """
    _message = message_db.get_message_by_id(session=db, id=message_id)
    _user_chat=get_user_chat(chat_id=_message.chat_id, user_id=user_id, db=db)
    if _user_chat is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вас нет в этом чате")

    _sender_id = message_db.get_sender_id(session=db, message_id=_message.id)
    if _sender_id != user_id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вам сюда нельзя")

    _message = message_db.update_message_by_id(session=db, id=_message.id, message=message)
    return _message


@router.delete("/{message_id}")
def delete_message(message_id: int, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Удалить сообщение по заданному message_id """
    _message = message_db.get_message_by_id(session=db, id=message_id)
    _user_chat=get_user_chat(chat_id=_message.chat_id, user_id=user_id, db=db)
    if _user_chat is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вас нет в этом чате")

    _sender_id = message_db.get_sender_id(session=db, message_id=_message.id)
    if _sender_id != user_id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вам сюда нельзя")

    _message = message_db.delete_message_by_id(session=db, id=_message.id)
    return _message