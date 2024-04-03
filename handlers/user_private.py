from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from common.additional import get_main_kb, get_invite_kb
from common.reply_messages import start_add_user, reply_referer, send_start_message, send_user_balance, \
    send_main_menu_kb, send_main_menu_kb_message
from config import BOT_LINK
from database.orm_query import orm_user_exists, orm_add_user, orm_user_exists, update_referer_id, orm_referer_add_token, \
    orm_get_current_balance
from filters.chat_types import ChatTypeFilter
from handlers.user_private_checked import user_private_checked
from kbds.inline import get_callback_btns, get_url_btns
from kbds.keyboards import get_kb

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))
user_private_router.include_router(user_private_checked)

@user_private_router.message(CommandStart())
async def start_message(message: types.Message, session: AsyncSession, bot: Bot):
    # get = await user_exists(session, 123213214)
    # print(f'ЭТО ВЫВОД - ', get)
    referal_link = message.text
    referer_id = referal_link[8:]
    print('Информационный вывод - ', len(referer_id))

    if await orm_user_exists(session, message.from_user.id) == None:
        if len(referer_id) == 0:
            await start_add_user(message, session=session, referer_id=referer_id)
        else:
            await orm_referer_add_token(session, referer_id)
            await reply_referer(message, referer_id, bot=bot)
            await start_add_user(message, session=session, referer_id=referer_id)
    else:
        # await update_referer_id(session, user_id=message.from_user.id, referer_id=referer_id)
        await send_main_menu_kb_message(message)
        await send_user_balance(message=message, session=session)


@user_private_router.callback_query(F.data == 'check_subscribe')
async def check_subscribe_command(callback: types.CallbackQuery, bot: Bot, session: AsyncSession):
    ref_link = f'{BOT_LINK}?start=r{callback.from_user.id}'

    current_balance = await orm_get_current_balance(session, user_id=callback.from_user.id)

    if (await bot.get_chat_member(chat_id='@hamitoken', user_id=callback.from_user.id)).status != 'left':
        await send_main_menu_kb(callback)

        await callback.message.answer_photo('AgACAgIAAxkBAAIBhWYLD_BBRjTVjvdMOmNZFki0knyDAAIX2zEbXu1ZSK1FJQr4kUB9AQADAgADeAADNAQ',
                                            caption=f'<b>Ваш баланс: {current_balance} $HAMI 🐹</b>\n1fren = 500 $HAMI\n\nЧтобы умножить ваш баланс на 2х, надо перейти во кладку Twitter\n\nПригласить друзей👇',
                                            reply_markup=get_invite_kb(ref_link))

        await callback.answer()
    else:
        await callback.message.answer('Сначала подпишись бля нефор')
        await callback.answer('Nope!')



@user_private_router.message(F.photo)
async def get_photo(message: types.Message):
    if message.photo:
        await message.answer(f'ID фото: {message.photo[-1].file_id}')