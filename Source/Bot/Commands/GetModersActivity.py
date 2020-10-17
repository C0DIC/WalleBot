from aiogram import types
from ..Bot import walle

async def get_moders_activity(msg: types.Message):
    try:
        chat = msg.chat.id
        chat_admins = [admin.user for admin in await walle.get_chat_administrators(chat)]

        await walle.send_message(-1001471262276, chat_admins)
    except Exception as e:
        print(e)