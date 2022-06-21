from sqlalchemy.orm import Session

from database.models import User as UserDB
from schemas.user import User
from security import get_password_hash, verify_password
from broker.redis import redis



def get_user_by_id(session: Session, id: int):
    user = session.query(UserDB).filter_by(id=id).one_or_none()
    return user


def get_user_by_login(session: Session, login: str):
    user = session.query(UserDB).filter_by(login=login).one_or_none()
    return user


def create_user(session: Session, user: User):
    hashed_password = get_password_hash(user.password)
    _user = UserDB(
        login = user.login,
        password = hashed_password,
        name = user.name
    )
    session.add(_user)
    session.commit()
    session.refresh(_user)
    return _user


def update_user_by_id(session: Session, id: int, user: User):
    _user = session.query(UserDB).filter_by(id=id).one_or_none()
    _user.login = user.login,
    _user.password = user.password,
    _user.name = user.name

    session.commit()
    session.refresh(_user)
    return _user


def delete_user_by_id(session: Session, id: int):
    _user = session.query(UserDB).filter_by(id=id).one_or_none()
    _user.is_deleted = True
    session.commit()
    session.refresh(_user)
    return _user


def authenticate(db: Session, login: str, password: str):
    _user = get_user_by_login(db, login)
    if not _user:
        return False
    if not verify_password(password, _user.password):
        return False

    pubsub = redis.pubsub()
    pubsub.subscribe(f"user-{_user.id}")
    return _user