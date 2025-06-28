from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import TaskIn
from app.models import Task

async def create_task(task_in: TaskIn, db: AsyncSession) -> Task:
    new_task = Task(**task_in.dict())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task