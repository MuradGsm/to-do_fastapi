from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserCreate, UserOut, UserLogin
from app.settings.database import get_session
from app.service.user_service import register_user_service, user_login_service
from app.dependencies.auth import get_current_user
from app.models.user_models import User
router = APIRouter(prefix='/user', tags=['Users'])



@router.post('/register', response_model=UserOut)
async def register_user(user:UserCreate, db: AsyncSession = Depends(get_session)):
    return await register_user_service(user, db)

@router.post('/login')
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_session)):
    return await user_login_service(user, db)

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email, "id": current_user.id}