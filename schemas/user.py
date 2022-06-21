from pydantic import BaseModel


class User(BaseModel):
    login: str
    name: str
    class Cinfig:
        orm_mode = True


class UserCreate(User):
    password: str


class UserInDB(User):
    id: int
