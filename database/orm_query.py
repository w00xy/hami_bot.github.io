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



async def orm_update_wallet(session: AsyncSession, data: dict, user_id):
    query = update(User).where(User.user_id == user_id).values(
        wallet_address=data['wallet_address']
    )
    await session.execute(query)
    await session.commit()


async def update_referer_id(session: AsyncSession, user_id, referer_id):
    query = update(User).where(User.user_id == user_id).values(
        referer_id=referer_id
    )
    await session.execute(query)
    await session.commit()


async def orm_get_current_balance(session: AsyncSession, user_id):
    query = select(User.balance).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.scalar()

async def orm_referer_add_token(session: AsyncSession, referer_id):
    current_balance = int(await orm_get_current_balance(session, user_id=referer_id))
    new_balance = current_balance + 500
    print(f'ЭТО ИНФ ВЫВОД - {new_balance}')
    query = update(User).where(User.user_id == referer_id).values(
        balance=new_balance
    )
    await session.execute(query)
    await session.commit()


async def orm_get_repost_link(session: AsyncSession, user_id):
    query = select(User.repost_link).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.scalar()

async def orm_update_repost_link(session: AsyncSession, user_id, data):
    query = update(User).where(User.user_id == user_id).values(
        repost_link=data['repost_link']
    )
    await session.execute(query)
    await session.commit()

