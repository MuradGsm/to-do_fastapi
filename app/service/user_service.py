from fastapi import HTTPException, status
from app.models.user_models import User
from app.schemas.user_schema import UserCreate, UserOut, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import hash_password, verify_password
from sqlalchemy import select

async def register_user_service(user:UserCreate, db: AsyncSession) -> User:
    stmt = select(User).filter(User.email == user.email)
    result = await db.execute(stmt)
    new_user = result.scalars().first()
    if new_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='A user with this email is already registered')
    hashed_pw = hash_password(user.password)
    new_user = User(email = user.email, hashed_password = hashed_pw)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def user_login_service(user: UserLogin, db: AsyncSession):
    stmt = select(User).filter(User.email == user.email)
    result = await db.execute(stmt)
    log_user = result.scalars().first()
    if log_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if not verify_password(user.password ,log_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The password or email is incorrect !')    
    return {'Message': 'token'}
    
