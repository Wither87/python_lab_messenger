from fastapi import APIRouter
from schemas.message import MessageInChatFromUser, MessageInDB
from schemas.message import Message, MessageType
from crud.user import user_database
from crud.chat import chat_database
from crud.message import message_database
from datetime import date

from fastapi import HTTPException


router = APIRouter(
    prefix="/message",
    tags=["message"]
)


@router.get("/{message_id}", response_model=MessageInChatFromUser)
async def get_message(message_id: int):
    """ Получить сообщение по message_id """

    # Поиск сообщения в базе
    message = message_database[message_id-1]
    # Поиск чата в базе
    chat_model = getChat(message["chat_id"])
    # Поиск пользователя в базе
    user_model = getUser(message["user_id"])
    
    return MessageInChatFromUser(message=message, chat=chat_model, user=user_model)


@router.post("/", response_model=MessageInDB)
async def create_message(message: Message, chat_id: int, user_id: int):
    """ Отправка сообщения в чат """
    # проверка что чат существует
    if getChat(chat_id) == None:
        raise HTTPException(status_code=404, detail=f"chat not found")

    # проверка что юзер существует
    if getUser(user_id) == None:
        raise HTTPException(status_code=404, detail=f"user not found")
    
    message_db = MessageInDB(id=len(message_database) + 1, chat_id=chat_id, user_id=user_id, **message.dict())
    # Здесь добавление в базу
    return message_db


@router.put("/")
async def update_message(message_id: int, message: Message, user_id: int):
    """ Изменение сообщения """
    # получаю id пользователя, кто отправил сообщение
    who_send_message_id = getSenderId(message_id)
    # проверяю id пользователя с id кто отправил сообщение
    if who_send_message_id != user_id:
        raise HTTPException(status_code=403, detail=f"no access")
        
    message_db = message_database[message_id-1]
    for param, value in message.dict().items():
        message_db[param] = value
    # Здесь запись изменений в базу
    return message_db


@router.delete("/{message_id}")
def delete_message(message_id: int, user_id: int):
    """ Удалить сообщение по заданному message_id """
    # получаю id пользователя, кто отправил сообщение
    who_send_message_id = getSenderId(message_id)
    # проверяю id пользователя с id кто отправил сообщение
    if who_send_message_id != user_id:
        raise HTTPException(status_code=403, detail=f"no access")

    db = list(message_database)
    del db[message_id]
    return db


def getSenderId(message_id):
    who_send_message_id = None
    for message_from_user in message_database:
        if message_from_user["message_id"] == message_id:
            who_send_message_id = message_from_user["user_id"]
            break
    return who_send_message_id


def getChat(chat_id):
    chat_model = None
    for chat in chat_database:
        if chat["id"] == chat_id:
            chat_model = chat
    return chat_model


def getUser(user_id):
    user_model = None
    for user in user_database:
        if user["id"] == user_id:
            user_model = user
    return user_model