from app.settings.database import Base, int_pk
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String



class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)  
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)      