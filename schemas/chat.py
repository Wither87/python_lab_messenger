from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    created_date: datetime
    type: ChatType

    class Cinfig:
        orm_mode = True