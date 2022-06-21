from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Message(Base):
    __tablename__ = "Messages"

    id = Column(Integer, primary_key=True)
    message_type = Column(String, nullable=False)
    text = Column(String)
    media = Column(String)
    send_date = Column(DateTime, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_modified = Column(Boolean, nullable=True, default=False)
    is_readed = Column(Boolean, nullable=True, default=False)

    chat_id = Column(Integer, ForeignKey("Chats.id"))
    user_id = Column(Integer, ForeignKey("Users.id"))
    Chat = relationship("Chat")
    User = relationship("User")

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)


class Chat(Base):
    __tablename__ = "Chats"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    type = Column(String, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    last_activity = Column(DateTime, nullable=False)


class UserChat(Base):
    __tablename__ = "UserChat"
    
    id = Column(Integer, primary_key=True)

    chat_id = Column(Integer, ForeignKey("Chats.id"))
    user_id = Column(Integer, ForeignKey("Users.id"))
    Chat = relationship("Chat")
    User = relationship("User")