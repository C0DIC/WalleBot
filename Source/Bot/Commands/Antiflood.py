import asyncio
from aiogram import types
from ..Bot import walle


data = []


async def antiflood(msg: types.Message):
    try:
        chat_id = msg.chat.id
        msg_id = msg.message_id
        sndr_id = msg.from_user.id
        chat_type = msg.chat.type

        if chat_type == 'supergroup':
            append_to_data = str(chat_id) + ':' + str(sndr_id) + ':' + str(msg_id)
            data.append(append_to_data)

        if len(data) >  7:
            await msg.answer("Flood detected (пожалуйста не обращайте внимания на это смс)")
            data.clear()

        print(data)
    except Exception as e:
        print(e)