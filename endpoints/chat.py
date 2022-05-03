from xml.dom.pulldom import CHARACTERS
from fastapi import APIRouter
from crud.chat import chat_database, user_chat_database
from schemas.chat import Chat, ChatInDB, ChatWithUsers
from schemas.user import User
from crud.user import user_database
from crud.message import message_database

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.get("/{chat_id}", response_model=ChatWithUsers)
async def get_chat(chat_id: int):
    """ Получить чат по заданному chat_id """
    chat = chat_database[chat_id-1]
    users_in_chat = []
    for user_chat in user_chat_database:
        if user_chat["chat_id"] == chat_id:
            for user in user_database:
                if user["id"] == user_chat["user_id"]:
                    users_in_chat.append(user)

    return ChatWithUsers(chat=chat, users=users_in_chat)


@router.post("/", response_model=ChatInDB)
async def create_chat(chat: Chat):
    """ Создать чат """
    chat_db = ChatInDB(id=len(chat_database) + 1, **chat.dict())
    return chat_db


@router.put("/", response_model=ChatInDB)
async def update_chat(chat_id: int, chat: Chat):
    """ Обновить чат """
    chat_db = chat_database[chat_id-1]
    for param, value in chat.dict().items():
        chat_db[param] = value

    # Здесь изменения сохраняются в базу
    return chat_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int):
    """ Удалить чат по заданному chat_id """
    db = list(chat_database)
    del db[chat_id]
    return db


@router.get("/last/{chat_id}")
async def get_last_messages_in_chat(chat_id: int, quantity: int = 10):
    """ Получить список последних сообщений в чате """
    # Получаю список сообщений в чате
    chat_messages = []
    for message in message_database:
        if message["chat_id"] == chat_id:
            chat_messages.append(message)
    # сортировка сообщений по дате отправки, в начале новые
    chat_messages = sorted(chat_messages, key=lambda dict: dict["send_date"], reverse=True)

    if quantity > len(chat_messages):
        quantity = len(chat_messages)
    return chat_messages[0:quantity]


@router.get("/activity/{chat_id}")
async def get_last_messages_in_chat(quantity: int = 10):
    """ Получить список чатов с последней активностью """
    
    messages_db = list(message_database)
    messages_db = sorted(messages_db, key = lambda dict: dict["send_date"], reverse=True)
    chat_ids = []
    for chat in messages_db:
        if chat["chat_id"] not in chat_ids:
            chat_ids.append(chat["chat_id"])
    
    chats = []
    for i in chat_ids:
        chats.append(await get_chat(i))

    if quantity > len(chat_database):
        quantity = len(chat_database)
    return chats[0:quantity]