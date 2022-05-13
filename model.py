from pydantic import BaseModel


class StaffInfo(BaseModel):
    staffName: str
    password: str
    email: str
    gender: str
    age: int
    phone: str
    dep_id: int


class LoginItem(BaseModel):
    staff_id: int
    password: str


class Token(BaseModel):
    access_token: str


class StaffID(BaseModel):
    staff_id: int
