from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User

async def orm_user_exists(session: AsyncSession, user_id: int):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.one_or_none()

async def orm_add_user(session: AsyncSession, user_id: int, referer_id: int, balance: int):
    session.add(User(
        user_id=user_id,
        referer_id=referer_id,
        balance=balance
    ))
    await session.commit()


async def orm_get_wallet_address(session: AsyncSession, user_id):
    query = select(User.wallet_address).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_add_wallet(session: AsyncSession, data: dict, ):

    await session.commit()


async def orm_update_wallet(session: AsyncSession, data: dict, user_id):
    query = update(User).where(User.user_id == user_id).values(
        wallet_address=data['wallet_address']
    )
    await session.execute(query)
    await session.commit()
