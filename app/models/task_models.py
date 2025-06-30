from app.settings.database import Base, int_pk
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean



class Task(Base):
    id: Mapped[int_pk]
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)