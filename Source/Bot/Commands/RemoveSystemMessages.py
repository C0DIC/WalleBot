from aiogram import types
from ..Bot import walle


async def remove_system_msg(msg: types.Message):
    try:
        await msg.answer(msg.reply_to_message.content_type)

        msg_type = msg.content_type
    
        if msg_type == 'pinned_message':
            await msg.delete()
    except Exception as e:
        print(e)