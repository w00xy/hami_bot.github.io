from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types

from kbds.inline import get_url_btns
from kbds.keyboards import get_kb
from emoji import emojize as _

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(_('Это Hami bot 🐹'), reply_markup=get_url_btns(btns={
                'Начать фармить': 'https://t.me/herewalletbot/app'
            }))
    await message.delete()