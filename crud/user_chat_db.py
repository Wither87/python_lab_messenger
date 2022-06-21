from sqlalchemy.orm import Session

from database.models import UserChat
from crud import chat_db


def get_user_chat_by_ids(session: Session, user_id: int, chat_id: int):
    _user_chat = session.query(UserChat) \
        .filter(UserChat.user_id == user_id, UserChat.chat_id == chat_id) \
        .one_or_none()
    return _user_chat