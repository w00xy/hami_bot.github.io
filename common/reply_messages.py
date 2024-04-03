from aiogram import types, Bot
from sqlalchemy.ext.asyncio import AsyncSession

from common.additional import get_main_kb, get_invite_kb
from config import BOT_LINK
from database.orm_query import orm_add_user, orm_get_current_balance
from kbds.inline import get_callback_btns, get_url_btns


async def send_start_message(message: types.Message):
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


async def start_add_user(message: types.Message, session: AsyncSession, referer_id):
    await orm_add_user(session, user_id=message.from_user.id, referer_id=referer_id, balance=500)
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


async def reply_referer(message: types.Message, referer_id, bot: Bot):
    referal_name = f'{message.from_user.first_name } {message.from_user.last_name}'
    await bot.send_message(chat_id=referer_id, text=f'Новый реферал - {referal_name}👥')


async def send_user_balance(message: types.Message, session: AsyncSession):
    ref_link = f'{BOT_LINK}?start=r{message.from_user.id}'
    current_balance = await orm_get_current_balance(session, message.from_user.id)
    text = "500 $HAMI for everybody🐹\nLet's grow the biggest community ever!"

    current_balance = await orm_get_current_balance(session, message.from_user.id)
    await message.answer_photo(
        'AgACAgIAAxkBAAIBhWYLD_BBRjTVjvdMOmNZFki0knyDAAIX2zEbXu1ZSK1FJQr4kUB9AQADAgADeAADNAQ',
        caption=f'<b>Ваш баланс: {current_balance} $HAMI 🐹</b>\n1fren = 500 $HAMI\n\nЧтобы умножить ваш баланс на 2х, надо перейти во кладку Twitter\n\nПригласить друзей👇',
        reply_markup=get_url_btns(
            btns={
                'Пригласить друга/invite👥': f'https://t.me/share/url?url={ref_link}&text={text}',
            }
        ))


async def send_main_menu_kb(callback):
    await callback.message.answer('<b>📃 Главное меню</b>',
                                  reply_markup=get_main_kb())


async def send_main_menu_kb_message(message: types.Message):
    await message.answer('<b>📃 Главное меню</b>',
                            reply_markup=get_main_kb())

async def send_terms(message: types.Message):
    ref_link = f'{BOT_LINK}?start=r{message.from_user.id}'

    await message.answer_photo('AgACAgIAAxkBAAIDyGYNk_NXyoL-EXQzygMr2hj35mzYAALB2DEb1R9oSFHF2tNuOo_nAQADAgADeAADNAQ',
                               caption=f'<b>Условия/Terms</b>📒\n\nЧто бы стать участником AIRDROP нужно быть подписанным на официальный телеграм канал главного хомяка - @hamitoken✅\n\nАбсолютно каждый получит токены $HAMI🐹\n\nЗа каждого приглашенного друга, подписавшегося на телеграм канал ты получшиь 500 $HAMI🔥\nЧто бы УДВОИТЬ свои токены выполни бонусное задание во вкладке Twitter(BONUS)📢\n\nВаша реферальная ссылка - {ref_link}\n\nНу или просто нажми на кнопку ниже что бы пригласить друга👇🏼',
                               reply_markup=get_invite_kb(ref_link))
