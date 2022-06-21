from sqlalchemy.orm import Session

from database.models import Chat as ChatDB
from schemas.chat import Chat


def get_chat_by_id(session: Session, id: int):
    _chat = session.query(ChatDB).filter_by(id=id).one_or_none()
    return _chat


def create_chat(session: Session, chat: Chat):
    _chat = ChatDB(
        name = chat.name,
        created_date = chat.created_date,
        type = chat.type,
        last_activity = chat.created_date
    )
    session.add(_chat)
    session.commit()
    session.refresh(_chat)
    return _chat


def update_chat_by_id(session: Session, id: int, chat: Chat):
    _chat = session.query(ChatDB).filter_by(id=id).one_or_none()
    _chat.name = chat.name
    _chat.type = chat.type
    _chat.created_date = chat.created_date    
    _chat.last_activity = chat.created_date

    session.commit()
    session.refresh(_chat)
    return _chat


def delete_chat_by_id(session: Session, id: int):
    _chat = session.query(ChatDB).filter_by(id=id).one_or_none()
    _chat.is_deleted = True
    session.commit()
    session.refresh(_chat)
    return _chat


def get_chat_list_with_last_activity(session: Session, quantity: int = 10):
    _chats = session.query(ChatDB) \
        .order_by(ChatDB.last_activity.desc()) \
        .limit(quantity)
    return _chats