from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User

async def user_exists(session: AsyncSession, user_id: int):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.one_or_none()

async def add_user(session: AsyncSession, user_id: int, referer_id: int, balance: int):
    session.add(User(
        user_id=user_id,
        referer_id=referer_id,
        balance=balance
    ))
    await session.commit()



