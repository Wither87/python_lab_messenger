from fastapi import APIRouter, Depends
from deps import get_db, get_current_user
from schemas.chat import Chat
from crud import chat_db, message_db

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.get("/{chat_id}")
async def get_chat(chat_id: int, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Получить чат по заданному chat_id """
    chat = chat_db.get_chat_by_id(session=db, id=chat_id)
    return chat


@router.post("/")
async def create_chat(chat: Chat, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Создать чат """
    _chat = chat_db.create_chat(session=db, chat=chat)
    return _chat


@router.put("/")
async def update_chat(chat_id: int, chat: Chat, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Обновить чат """
    _chat = chat_db.update_chat_by_id(session=db, id=chat_id, chat=chat)
    return _chat


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Удалить чат по заданному chat_id """
    _chat = chat_db.delete_chat_by_id(chat_id)
    return _chat


@router.get("/last/{chat_id}")
async def get_last_messages_in_chat(chat_id: int, quantity: int = 10, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Получить список последних сообщений в чате """
    _chat = chat_db.get_chat_by_id(chat_id)
    _messages = []
    for _message in message_db.get_messages_by_chat_id(session=db, chat_id=chat_id, quantity=quantity):
        _messages.append(_message)
    return (_chat, _messages)


@router.get("/activity/{chat_id}")
async def get_last_activity_in_chat(quantity: int = 10, user_id=Depends(get_current_user), db=Depends(get_db)):
    """ Получить список чатов с последней активностью """
    _chats = []
    for _chat in chat_db.get_chat_list_with_last_activity(session=db, quantity=quantity):
        _chats.append(_chat)
    return _chats