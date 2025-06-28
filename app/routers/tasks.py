from fastapi import APIRouter, Depends
from app.crud import create_task
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas import TaskIn, TaskOut

router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.post('/create', response_model=TaskOut)
async def create(task_in: TaskIn, db: AsyncSession = Depends(get_session)):
    return await create_task(task_in, db)
