from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: str
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: str
    password: str
