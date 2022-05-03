from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from schemas.user import UserInDB
from schemas.chat import ChatInDB


class MessageType(str, Enum):
    text = "text"
    media = "media"


class Message(BaseModel):
    message_type: MessageType
    text: str
    media: str
    send_date: datetime


class MessageInDB(Message):
    chat_id: int
    user_id: int
    id: int


class MessageInChatFromUser(BaseModel):
    message: Message
    chat: ChatInDB
    user: UserInDB
