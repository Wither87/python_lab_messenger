from pydantic import BaseModel
from datetime import datetime
from enum import Enum
import json


class MessageType(str, Enum):
    text = "text"
    media = "media"


class Message(BaseModel):
    message_type: MessageType
    text: str
    media: str
    send_date: datetime

    class Cinfig:
        orm_mode = True