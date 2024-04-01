from aiogram.filters import Filter
from aiogram import Bot, types


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        return message.from_user.id in [1072341012, 1098796632] #bot.my_admins_list


class Subscribed(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        user_channel_status = await bot.get_chat_member(chat_id='@hamitoken', user_id=message.from_user.id)
        return user_channel_status.status != 'left'


class Subscribed_callback(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, callback: types.CallbackQuery, bot: Bot) -> bool:
        user_channel_status = await bot.get_chat_member(chat_id='@hamitoken', user_id=callback.from_user.id)
        return user_channel_status.status != 'left'
