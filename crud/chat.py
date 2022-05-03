from datetime import datetime
from schemas.chat import ChatType



user_chat_database = [
    {
        "user_id": 1,
        "chat_id": 1
    },
    {
        "user_id": 2,
        "chat_id": 1
    },
    {
        "user_id": 1,
        "chat_id": 2
    },
    {
        "user_id": 2,
        "chat_id": 2
    },
    {
        "user_id": 1,
        "chat_id": 3
    },
    {
        "user_id": 2,
        "chat_id": 3
    }
]


chat_database = [
    {
        "id": 1,
        "name": "Чат_1",
        "created_date": datetime(2022, 4, 20, 19, 39, 0),
        "type": ChatType.group
    },
    {
        "id": 2,
        "name": "Чат_2",
        "created_date": datetime(2022, 4, 20, 19, 39, 0),
        "type": ChatType.group
    },
    {
        "id": 3,
        "name": "Чат_3",
        "created_date": datetime(2022, 4, 20, 19, 39, 0),
        "type": ChatType.group
    }
]

