from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.ext.asyncio import AsyncSession

from common.additional import get_main_kb
from common.reply_messages import send_user_balance, send_terms, send_main_menu_kb_message
from config import BOT_LINK
from database.orm_query import orm_get_wallet_address, orm_update_wallet, orm_get_current_balance, orm_get_repost_link, \
    orm_update_repost_link
from filters.chat_types import ChatTypeFilter, Subscribed
from kbds.inline import get_url_btns, get_callback_btns
from kbds.keyboards import get_kb

# создаем роутер
user_private_checked = Router()
user_private_checked.message.filter(ChatTypeFilter(["private"]), Subscribed())
user_private_checked.callback_query.filter(Subscribed())



@user_private_checked.message(F.text == 'Кошелек/Wallet👛')
async def send_wallet_command(message: types.Message, session: AsyncSession, state: FSMContext):
    wallet_address = await orm_get_wallet_address(session, user_id=message.from_user.id)

    caption = f'📝 Вам нужно привязать НЕкастодиальный кошелек сети TON. Рекомендуем - Tonkeeper\n\nТвой кошелек - Пусто...'
    wif_wallet_caption = f'📝 Твой кошелек - {wallet_address}'

    if not wallet_address:
        await message.answer_photo(
            'AgACAgIAAxkBAAIB3WYMVGy8X-TTdkAHrjiOFQ79dhvuAAJ3MTIbzW1gSH5BhXyrtlRLAQADAgADeQADNAQ',
            caption=caption)
        await message.answer('Пришли адрес твоего кошелька TON:',
                             reply_markup=get_kb(
                                 '🚫 Отмена'
                             ))
        await state.set_state(AddWallet.wallet)
    else:
        await message.answer_photo('AgACAgIAAxkBAAIB3WYMVGy8X-TTdkAHrjiOFQ79dhvuAAJ3MTIbzW1gSH5BhXyrtlRLAQADAgADeQADNAQ',
                                   caption=wif_wallet_caption,
                                   reply_markup=get_callback_btns(
                                       btns={
                                           'Изменить адрес/Change📝' : 'change_wallet_address'
                                       },
                                        sizes=(1,),
                                   ))


@user_private_checked.callback_query(F.data == 'change_wallet_address')
async def send_change_wallet(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Пришли адрес твоего кошелька TON:',
                         reply_markup=get_kb(
                             '🚫 Отмена'
                         ))
    await callback.answer('')
    await state.set_state(AddWallet.wallet)


@user_private_checked.message(F.text == '🚫 Отмена')
async def send_main_menu(message: types.Message, session: AsyncSession):
    ref_link = f'{BOT_LINK}?start=r{message.from_user.id}'
    current_balance = await orm_get_current_balance(session, message.from_user.id)
    text = "500 $HAMI for everybody🐹\nLet's grow the biggest community ever!"

    await message.answer('<b>📃 Главное меню</b>',
                                  reply_markup=get_main_kb()
                                  )
    await message.answer_photo(
        'AgACAgIAAxkBAAIBhWYLD_BBRjTVjvdMOmNZFki0knyDAAIX2zEbXu1ZSK1FJQr4kUB9AQADAgADeAADNAQ',
        caption=f'<b>Ваш баланс: {current_balance} $HAMI 🐹</b>\n1fren = 500 $HAMI\n\nЧтобы умножить ваш баланс на 2х, надо перейти во кладку Twitter\n\nПригласить друзей👇',
        reply_markup=get_url_btns(
            btns={
                'Пригласить друга/invite👥': f'https://t.me/share/url?url={ref_link}&text={text}',
            }
        ))

class AddWallet(StatesGroup):
    wallet = State()


@user_private_checked.message(AddWallet.wallet)
async def add_wallet(message: types.Message, state: FSMContext, session: AsyncSession):
    if len(message.text) > 15:
        await state.update_data(wallet_address=message.text)
        data = await state.get_data()
        try:
            await orm_update_wallet(session, data, user_id=message.from_user.id)
            await message.answer(f'Адрес вашего кошелька был сохранен - {message.text}\n\nЕсли вы хотите его изменить перейдите еще раз во вкладку Кошелек🐹', )
            await send_main_menu_kb_message(message)
            await state.clear()
        except Exception as e:
            await message.answer('гг сломал бота')
            await state.clear()
    else:
        await message.answer('Ты чето не то кинул, попробуй еще раз')




@user_private_checked.message(F.text == 'Баланс/balance🐹')
async def user_balance(message: types.Message, session: AsyncSession):
    await send_user_balance(message=message, session=session)


class AddRepostLink(StatesGroup):
    add_repost_link = State()

@user_private_checked.message(F.text == 'Twitter(BONUS)📢')
async def user_balance(message: types.Message, session: AsyncSession, state: FSMContext):
    repost_link = await orm_get_repost_link(session, message.from_user.id,)

    if repost_link:
        await message.answer_photo(
            'AgACAgIAAxkBAAIDOGYNS_Lmpg6b2Lj4iRag71ZGGcmdAALs1jEb1R9oSAKOsoLN8ccIAQADAgADeQADNAQ',
            caption=f'Выполнив бонусное задание баланс будет умножен x2!😱\nСделай репост поста в твиттере - *здесь будет ссылка на пост*\n\nБАЛАНС БУДЕТ УМНОЖЕН ПОСЛЕ ОКОНЧАНИЯ AIRDROP!\n\nСсылка на ваш репост:\n{repost_link}',
            reply_markup=get_callback_btns(
                btns={
                    'Изменить ссылку/Change📝': 'change_link'
                },
                sizes=(1,),
            ))
    else:
        await message.answer_photo(
            'AgACAgIAAxkBAAIDOGYNS_Lmpg6b2Lj4iRag71ZGGcmdAALs1jEb1R9oSAKOsoLN8ccIAQADAgADeQADNAQ',
            caption=f'Выполнив бонусное задание баланс будет умножен x2!😱\nСделай репост поста в твиттере - *здесь будет ссылка на пост*\n\nБАЛАНС БУДЕТ УМНОЖЕН ПОСЛЕ ОКОНЧАНИЯ AIRDROP!\n\nСсылка на ваш репост:\n',
            )
        await message.answer('Пришли ссылку на свой ретвит:',
                             reply_markup=get_kb(
                                 '🚫 Отмена'
                             ))
        await state.set_state(AddRepostLink.add_repost_link)

@user_private_checked.callback_query(F.data == 'change_link')
async def change_user_repost_link(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Пришли ссылку на свой ретвит:',
                         reply_markup=get_kb(
                             '🚫 Отмена'
                         ))

    await callback.answer('')
    await state.set_state(AddRepostLink.add_repost_link)


@user_private_checked.message(AddRepostLink.add_repost_link)
async def get_user_repost_link(message: types.Message, session: AsyncSession, state: FSMContext):
    if len(message.text) > 12:
        await state.update_data(repost_link=message.text)
        data = await state.get_data()
        try:
            await orm_update_repost_link(session, user_id=message.from_user.id, data=data)
            await message.answer(
                f'Cсылка на репорст сохранена - {message.text}\n\nЕсли вы хотите ее изменить перейдите еще раз во вкладку Twitter🐹', )
            await send_main_menu_kb_message(message)
            await state.clear()
        except Exception as e:
            await message.answer('гг сломал бота')
            await state.clear()
    else:
        await message.answer('Ты чето не то кинул, попробуй еще раз')



@user_private_checked.message(F.text == 'Условия/Terms📒')
async def send_terms_airdrop(message: types.Message):
    await send_terms(message)