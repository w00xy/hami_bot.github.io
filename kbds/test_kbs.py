from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from emoji import emojize as _

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
         ],
        [
            KeyboardButton(text='Варианты доставки'),
            KeyboardButton(text='Варианты оплаты'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text=_('Меню:books:')),
    KeyboardButton(text=_('О магазине:shopping_cart:')),
    KeyboardButton(text=_('Варианты доставки:rocket:')),
    KeyboardButton(text=_('Варианты оплаты:money_with_wings:'))
)
start_kb2.adjust(2, 2)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Оставить отзыв'))
start_kb3.adjust(2, 2)
