from sqlalchemy.orm import Session

from database.models import Message as MessageDB, Chat
from schemas.message import Message


def get_message_by_id(session: Session, id: int):
    _message = session.query(MessageDB).filter_by(id=id).one_or_none()
    return _message


def create_message(session: Session, user_id, chat_id, message: Message):
    _message = MessageDB(
        chat_id=chat_id, 
        user_id=user_id, 
        message_type=message.message_type, 
        text=message.text,
        media=message.media, 
        send_date=message.send_date
    )
    session.add(_message)
    _chat = session.query(Chat).filter_by(id=chat_id).one_or_none()
    _chat.last_activity = message.send_date

    session.commit()
    session.refresh(_message)
    return _message


def update_message_by_id(session: Session, id: int, message: Message):
    _message = session.query(MessageDB).filter_by(id=id).one_or_none()
    _message.message_type=message.message_type
    _message.text=message.text
    _message.media=message.media

    if not _message.is_modified:
        _message.is_modified = True 

    session.commit()
    session.refresh(_message)
    return _message


def delete_message_by_id(session: Session, id: int):
    _message = session.query(MessageDB).filter_by(id=id).one_or_none()
    _message.is_deleted = True
    session.commit()
    session.refresh(_message)
    return _message


def get_sender_id(session: Session, message_id: int):
    _message = session.query(MessageDB).filter_by(id=message_id).one_or_none()
    return _message.user_id


def get_messages_by_chat_id(session: Session, chat_id: int, quantity = 10):
    _messages = session.query(MessageDB) \
        .filter_by(chat_id=chat_id) \
        .order_by(Message.id.desc()) \
        .limit(quantity)
    return _messages


def set_readed(session: Session, message_id: int):
    _message = get_message_by_id(message_id)

    if not _message.is_readed:
        _message.is_readed = True
        session.commit()
        session.refresh(_message)