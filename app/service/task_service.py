from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.task_schemas import TaskIn, TaskUpdate
from app.models.task_models import Task
from typing import List, Optional
from app.utils import get_task_utils

async def create_task_service(task_in: TaskIn, db: AsyncSession) -> Task:
    new_task = Task(**task_in.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


async def get_all_tasks_service(db: AsyncSession, is_done: Optional[bool] = None) -> List[Task]:
    stmt  = select(Task)
    if is_done is not None:
        stmt = stmt.where(Task.is_done == is_done)
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

async def delete_task_service(task_id: int, db: AsyncSession) -> dict:
    task = await get_task_service(task_id, db)
    await db.delete(task)
    await db.commit()
    return {"Message": "Delete succesfully"}

