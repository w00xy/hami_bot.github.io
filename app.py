import asyncio
import logging
import os

from database.engine import drop_db, create_db, session_maker

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from common.bot_cmds_list import private
from common.routers import routers
from config import TOKEN
from middlewares.db import DataBaseSession

# разрешенные методы общения с ботом
allowed_updates = ['message, callback_query']

# creating database
async def on_startup():

    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown():
    print('Бот лёг')


async def main():
    # bot setting
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    bot.my_admins_list = []

    dp = Dispatcher()

    # on_start_up and shotdown functions dasdsa
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # drop offline messages
    await bot.delete_webhook(drop_pending_updates=True)

    # подключение роутеров
    for router in routers:
        dp.include_router(router)

    # connecting the middlewares
    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    # кнопки из меню справа снизу
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

    await dp.start_polling(bot, allowed_updates=allowed_updates)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
