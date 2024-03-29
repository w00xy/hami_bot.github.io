from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from kbds.inline import get_inlineMix_btns, get_url_btns, get_callback_btns


# создаем роутер
user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    # await message.answer(_('Это Hami bot 🐹'), reply_markup=get_url_btns(btns={
    #             'Начать фармить': 'https://t.me/herewalletbot/app'
    #         }))

    # Отвечаем пользователю картинкой + кнопки
    await message.answer_photo(
        photo='AgACAgIAAxkBAAM8ZgaLH-oBdfCl-QAB6gXQ4m4wfJ8VAAJn2TEbzOg4SI9Pnv-H3fZTAQADAgADeAADNAQ',
        caption='<b>AIRDROP HAMI COIN</b> 🐹\n\n500$HAMI - за каждого приглашенного в бота 🤝\nУспей позвать как можно больше друзей!\n\nНЕТ никаких ограничений, каждый получит гарантированный AIRDROP от HAMI🐹\nПодписывайся на официальный тг канал и читай условия, там все условия👇\n\n'
                'https://t.me/hamitoken',
        reply_markup=get_callback_btns(
            btns={
                'Присоединился✅': 'check_subscribe'
            },
            sizes=(1,)
        ))

    await message.delete()

# Проверка подписки на канал
@user_private_router.callback_query(F.data == 'check_subscribe')
async def check_subs(callback: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id='@hamitoken', user_id=callback.from_user.id)
    print(user_channel_status)
    print(user_channel_status)

    if user_channel_status.status == 'left':
        await callback.message.answer('Ты еще не подписался, давай подписывайся👇',
                                      reply_markup=get_inlineMix_btns(
                                          btns={
                                              'Перейти в канал🐹': 'https://t.me/hamitoken',
                                              'Присоединился✅': 'check_subscribe'
                                          },
                                          sizes=(1,)))
        await callback.answer('')
    else:
        await callback.message.answer('Круто, твой хомяк ждет тебя!',
                                      reply_markup=get_url_btns(
                                          btns={
                                              'Начать фармить': 'https://t.me/herewalletbot/app'
                                          }))
        await callback.answer('')



# Это вспомогательная функцию кидаешь фото получаешь его хэш


@user_private_router.message(Command('app'))
async def get_photo(message: Message):
    await message.answer('t.me/testwebbaappbot/webapptestdz')

@user_private_router.message()
async def get_photo(message: Message):
    if message.photo:
        await message.answer(f'ID фото: {message.photo[-1].file_id}')