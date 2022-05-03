from datetime import datetime
from schemas.message import MessageType

message_database = [
    {
        "message_id": 1,
        "chat_id": 1,
        "user_id": 1,
        "message_type": MessageType.text,
        "text": "Текст сообщения 1",
        "media": "",
        "send_date": datetime(2022, 4, 20, 20, 19, 0)
    },
    {
        "message_id": 2,
        "user_id": 1,
        "chat_id": 2,
        "message_type": MessageType.text,
        "text": "Текст сообщения 2",
        "media": "",
        "send_date": datetime(2022, 4, 20, 18, 50, 0)
    },
    {
        "message_id": 3,
        "user_id": 1,
        "chat_id": 2,
        "message_type": MessageType.text,
        "text": "Текст сообщения 3",
        "media": "",
        "send_date": datetime(2022, 4, 20, 18, 51, 0)
    },
    {
        "message_id": 4,
        "user_id": 1,
        "chat_id": 3,
        "message_type": MessageType.text,
        "text": "Текст сообщения 4",
        "media": "",
        "send_date": datetime(2022, 4, 20, 18, 51, 1)
    },
    {
        "message_id": 5,
        "user_id": 1,
        "chat_id": 3,
        "message_type": MessageType.text,
        "text": "Текст сообщения 5",
        "media": "",
        "send_date": datetime(2022, 4, 20, 19, 49, 34)
    }    
]
