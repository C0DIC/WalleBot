import asyncio
from aiogram import types
from ..Bot import walle


async def antiflood(msg: types.Message):
    try:
        msg_start = {msg.from_user.first_name : msg.message_id}
        await asyncio.sleep(7)
        msg_stop = {msg.from_user.first_name : msg.message_id}

    except Exception as e:
        print(e)