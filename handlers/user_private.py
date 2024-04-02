from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from config import BOT_LINK
from database.orm_query import user_exists, add_user
from filters.chat_types import ChatTypeFilter
from kbds.inline import get_callback_btns, get_url_btns
from kbds.keyboards import get_kb

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))

@user_private_router.message(CommandStart())
async def start_message(message: types.Message, session: AsyncSession):
    # get = await user_exists(session, 123213214)
    # print(f'ЭТО ВЫВОД - ', get)
    referer_id = None

    if await user_exists(session, message.from_user.id) == None:
        await add_user(session, user_id=message.from_user.id, referer_id=referer_id, balance=500)
        await message.answer_photo(
            photo='AgACAgIAAxkBAAM8ZgaLH-oBdfCl-QAB6gXQ4m4wfJ8VAAJn2TEbzOg4SI9Pnv-H3fZTAQADAgADeAADNAQ',
            caption='<b>AIRDROP HAMI TOKEN</b> 🐹\n\n<b>500</b> $HAMI - за каждого приглашенного в бота 🤝\nУспей позвать как можно больше друзей!\n\nНЕТ никаких ограничений, каждый получит гарантированный AIRDROP от HAMI🐹\nПодписывайся на официальный тг канал, там все условия👇\n\n'
                    '@hamitoken',
            reply_markup=get_callback_btns(
                btns={
                    'Присоединился✅': 'check_subscribe'
                },
                sizes=(1,)
            ))

        await message.delete()

    await message.answer_photo(
        photo='AgACAgIAAxkBAAM8ZgaLH-oBdfCl-QAB6gXQ4m4wfJ8VAAJn2TEbzOg4SI9Pnv-H3fZTAQADAgADeAADNAQ',
        caption='<b>AIRDROP HAMI TOKEN</b> 🐹\n\n<b>500</b> $HAMI - за каждого приглашенного в бота 🤝\nУспей позвать как можно больше друзей!\n\nНЕТ никаких ограничений, каждый получит гарантированный AIRDROP от HAMI🐹\nПодписывайся на официальный тг канал, там все условия👇\n\n'
                '@hamitoken',
        reply_markup=get_callback_btns(
            btns={
                'Присоединился✅': 'check_subscribe'
            },
            sizes=(1,)
        ))


@user_private_router.callback_query(F.data == 'check_subscribe')
async def check_subscribe_command(callback: types.CallbackQuery, bot: Bot):
    ref_link = f'{BOT_LINK}?start=r{callback.from_user.id}'
    text = "500 $HAMI for everybody🐹\nLet's grow the biggest community ever!"

    if (await bot.get_chat_member(chat_id='@hamitoken', user_id=callback.from_user.id)).status != 'left':
        await callback.message.answer('<b>📃 Главное меню</b>',
                                      reply_markup=get_kb('Кошелек/Wallet👛',
                                                          'Баланс/balance🐹',
                                                          'Twitter(HOT)📢',
                                                          'Условия/Terms📒',
                                                          placeholder='Выберай кнопку',
                                                          sizes=(2, 2,)
                                                          )
        )

        await callback.message.answer_photo('AgACAgIAAxkBAAIBhWYLD_BBRjTVjvdMOmNZFki0knyDAAIX2zEbXu1ZSK1FJQr4kUB9AQADAgADeAADNAQ',
                                            caption='<b>Ваш баланс: 500 $HAMI 🐹</b>\n1fren = 500 $HAMI\n\nЧтобы умножить ваш баланс на 2х, надо перейти во кладку Twitter\n\nПригласить друзей👇',
                                            reply_markup=get_url_btns(
                                                btns={
                                                    'Пригласить друга/invite👥' : f'https://t.me/share/url?url={ref_link}&text={text}',
                                                }
                                            ))

        await callback.answer()
    else:
        await callback.message.answer('Сначала подпишись бля нефор')
        await callback.answer('Nope!')


@user_private_router.message()
async def get_photo(message: types.Message):
    if message.photo:
        await message.answer(f'ID фото: {message.photo[-1].file_id}')