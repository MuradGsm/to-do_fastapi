from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserCreate, UserOut, UserLogin
from app.settings.database import get_session
from app.service.user_service import register_user_service, user_login_service

router = APIRouter(prefix='/user', tags=['Users'])



@router.post('/register', response_model=UserOut)
async def register_user(user:UserCreate, db: AsyncSession = Depends(get_session)):
    return await register_user_service(user, db)

@router.post('/login')
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_session)):
    return await user_login_service(user, db)