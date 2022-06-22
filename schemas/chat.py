from pydantic import BaseModel
from datetime import datetime
from enum import Enum

from schemas.message import MessageInDB


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    created_date: datetime
    type: ChatType

    class Config:
        orm_mode = True


class ChatInDB(Chat):
    id: int


class LastMessages(BaseModel):
    chat: ChatInDB
    messages: list[MessageInDB]

    class Config:
        orm_mode = True
