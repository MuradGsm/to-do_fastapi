from fastapi import APIRouter, Depends
from app.crud import create_task_service, get_all_tasks_service, get_task_service, update_task_service
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas import TaskIn, TaskOut, TaskUpdate
from typing import List

router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.post('/create', response_model=TaskOut)
async def create_task(task_in: TaskIn, db: AsyncSession = Depends(get_session)):
    return await create_task_service(task_in, db)

@router.get('/all', response_model=List[TaskOut])
async def get_all_task(db: AsyncSession = Depends(get_session)):
    return await get_all_tasks_service(db)

@router.get('/{task_id}', response_model=TaskOut)
async def get_task(task_id: int, db: AsyncSession = Depends(get_session)):
    return await get_task_service(task_id, db)

@router.put('/{task_id}/update', response_model=TaskOut)
async def update_task(task_id: int, task_in: TaskUpdate, db: AsyncSession = Depends(get_session)):
    return await update_task_service(task_id, task_in, db)