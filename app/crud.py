from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import TaskIn, TaskUpdate
from app.models import Task
from typing import List
from app.utils import get_task_utils

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
    task = await get_task_utils(task_id, db)
    return task
    
async def update_task_service(task_id: int, task_in: TaskUpdate, db: AsyncSession) -> Task:
    task = await get_task_utils(task_id, db)
    
    for failed ,value in task_in.dict().items():
        setattr(task, failed, value )

    await db.commit()
    await db.refresh(task)
    return task

