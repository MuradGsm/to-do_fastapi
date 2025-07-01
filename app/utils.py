from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task_models import Task
from passlib.context import CryptContext

async def get_task_utils(task_id: int, db: AsyncSession):
    stmt = select(Task).filter(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalars().first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found!')
    return task


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)