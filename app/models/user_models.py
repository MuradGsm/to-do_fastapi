from app.settings.database import Base, int_pk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List


class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)  
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)      
    tasks: Mapped[List['Task']] = relationship(back_populates='user')