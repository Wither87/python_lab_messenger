from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import List
from schemas.user import User, UserInDB


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    created_date: datetime
    type: ChatType


class ChatInDB(Chat):
    id: int


class ChatWithUsers(BaseModel):
    chat: Chat
    users: List[UserInDB]