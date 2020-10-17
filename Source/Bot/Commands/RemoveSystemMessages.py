from aiogram import types
from ..Bot import walle


async def remove_system_msg(msg: types.Message):
    try:
        msg_type = msg.content_type

        if msg:
            if msg_type == 'pinned_message':
                msg.delete()
            else:
                pass
    except Exception as e:
        print(e)