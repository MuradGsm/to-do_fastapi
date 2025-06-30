from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import TaskIn
from app.models import Task
from typing import List

async def create_task_service(task_in: TaskIn, db: AsyncSession) -> Task:
    new_task = Task(**task_in.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


async def get_all_tasks_service(db: AsyncSession) -> List[Task]:
    stmt  = select(Task)
    result = await db.execute(stmt)
    tasks = result.scalars().all()
    return tasks

async def get_task_service(task_id: int, db: AsyncSession) -> Task:
    stmt = select(Task).filter(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalars().first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found!')
    return task
    