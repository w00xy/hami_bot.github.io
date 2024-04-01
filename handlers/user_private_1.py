from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import add_user, user_exists
from filters.chat_types import ChatTypeFilter, Subscribed
from kbds.inline import get_inlineMix_btns, get_url_btns, get_callback_btns


# создаем роутер
user_private1_router = Router()
user_private1_router.message.filter(ChatTypeFilter(["private"]), Subscribed())
user_private1_router.callback_query.filter(Subscribed())


# @user_private1_router.message(CommandStart)
# async def start_message(message: types.Message, session: AsyncSession):
#     # get = await user_exists(session, 123213214)
#     # print(f'ЭТО ВЫВОД - ', get)
#     referer_id = None
#
#     if await user_exists(session, message.from_user.id) == None:
#         await add_user(session, user_id=message.from_user.id, referer_id=referer_id, balance=500)
#         await message.answer_photo(
#             photo='AgACAgIAAxkBAAM8ZgaLH-oBdfCl-QAB6gXQ4m4wfJ8VAAJn2TEbzOg4SI9Pnv-H3fZTAQADAgADeAADNAQ',
#             caption='<b>AIRDROP HAMI TOKEN</b> 🐹\n\n<b>500</b> $HAMI - за каждого приглашенного в бота 🤝\nУспей позвать как можно больше друзей!\n\nНЕТ никаких ограничений, каждый получит гарантированный AIRDROP от HAMI🐹\nПодписывайся на официальный тг канал, там все условия👇\n\n'
#                     '@hamitoken',
#             reply_markup=get_callback_btns(
#                 btns={
#                     'Присоединился✅': 'check_subscribe'
#                 },
#                 sizes=(1,)
#             ))
#
#         await message.delete()
#
#     await message.answer_photo(
#         photo='AgACAgIAAxkBAAM8ZgaLH-oBdfCl-QAB6gXQ4m4wfJ8VAAJn2TEbzOg4SI9Pnv-H3fZTAQADAgADeAADNAQ',
#         caption='<b>AIRDROP HAMI TOKEN</b> 🐹\n\n<b>500</b> $HAMI - за каждого приглашенного в бота 🤝\nУспей позвать как можно больше друзей!\n\nНЕТ никаких ограничений, каждый получит гарантированный AIRDROP от HAMI🐹\nПодписывайся на официальный тг канал, там все условия👇\n\n'
#                 '@hamitoken',
#         reply_markup=get_callback_btns(
#             btns={
#                 'Присоединился✅': 'check_subscribe'
#             },
#             sizes=(1,)
#         ))


@user_private1_router.message(F.text == 'саня лох')
async def check_subs(message: types.Message, bot: Bot):
    await message.answer('Подтверждаю!')