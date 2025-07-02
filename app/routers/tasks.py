from fastapi import APIRouter, Depends
from app.service.task_service import (create_task_service, 
                      get_all_tasks_service, 
                      get_task_service, 
                      update_task_service, 
                      delete_task_service)
from sqlalchemy.ext.asyncio import AsyncSession
from app.settings.database import get_session
from app.schemas.task_schemas import TaskIn, TaskOut, TaskUpdate
from typing import List, Optional
from app.dependencies.auth import get_current_user
from app.models.user_models import User

router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.post('/create', response_model=TaskOut)
async def create_task(task_in: TaskIn, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    return await create_task_service(task_in,current_user ,db)

@router.get('/all', response_model=List[TaskOut])
async def get_all_task(db: AsyncSession = Depends(get_session),current_user:User = Depends(get_current_user), is_done: Optional[bool] = None):
    return await get_all_tasks_service(db,current_user, is_done)

@router.get('/{task_id}', response_model=TaskOut)
async def get_task(task_id: int,current_user: User = Depends(get_current_user) , db: AsyncSession = Depends(get_session)):
    return await get_task_service(task_id,current_user, db)

@router.put('/{task_id}/update', response_model=TaskOut)
async def update_task(task_id: int, task_in: TaskUpdate,current_user: User = Depends(get_current_user),  db: AsyncSession = Depends(get_session)):
    return await update_task_service(task_id, task_in,current_user, db)

@router.delete('/{task_id}/delete')
async def delete_task(task_id: int,current_user: User = Depends(get_current_user),  db: AsyncSession = Depends(get_session)):
    return await delete_task_service(task_id,current_user, db)