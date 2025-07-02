from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.task_schemas import TaskIn, TaskUpdate
from app.models.task_models import Task
from typing import List, Optional
from app.utils.utils import get_task_utils
from app.models.user_models import User

async def create_task_service(task_in: TaskIn,current_user: User , db: AsyncSession) -> Task:
    new_task = Task(
        title = task_in.title,
        description = task_in.description,
        is_done = task_in.is_done,
        user_id = current_user.id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


async def get_all_tasks_service(db: AsyncSession,current_user: User , is_done: Optional[bool] = None) -> List[Task]:
    stmt  = select(Task).where(Task.user_id == current_user.id)
    if is_done is not None:
        stmt = stmt.where(Task.is_done == is_done)
    result = await db.execute(stmt)
    tasks = result.scalars().all()
    return tasks

async def get_task_service(task_id: int,current_user: User, db: AsyncSession) -> Task:
    task = await get_task_utils(task_id,current_user, db)
    return task
    
async def update_task_service(task_id: int, task_in: TaskUpdate,current_user: User, db: AsyncSession) -> Task:
    task = await get_task_utils(task_id, current_user,db )
    
    for field ,value in task_in.dict(exclude_unset=True).items():
        setattr(task, field, value)

    await db.commit()
    await db.refresh(task)
    return task

async def delete_task_service(task_id: int,current_user: User, db: AsyncSession) -> dict:
    task = await get_task_service(task_id,current_user, db)
    await db.delete(task)
    await db.commit()
    return {"Message": "Delete succesfully"}

