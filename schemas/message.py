from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class MessageType(str, Enum):
    text = "text"
    media = "media"


class Message(BaseModel):
    message_type: MessageType
    text: str
    media: str
    send_date: datetime

    class Config:
        orm_mode = True


class MessageInDB(Message):
    id: int