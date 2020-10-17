from aiogram import types
from ..Bot import walle

async def get_moders_activity(msg: types.Message):
    try:
        chat = msg.chat.id
        chat_admins = [admin.user.first_name for admin in await walle.get_chat_administrators(chat)]

        admins = dict(admin: 0 for admin in chat_admins)

        print(admins)

        await walle.send_message(-1001471262276, chat_admins)
    except Exception as e:
        print(e)