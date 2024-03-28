from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types

from kbds.inline import get_url_btns
from emoji import emojize as _

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    markup=get_url_btns(btns={
                'Начать фармить': 't.me/testwebbaappbot/webapptestdz'
            })
    await message.answer(_('Это Hami bot 🐹'), reply_markup=markup)
    await message.delete()