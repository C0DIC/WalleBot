from aiogram import types
from ..Bot import walle


async def remove_system_msg(msg: types.Message):
    try:
        await msg.delete()
    except Exception as e:
        print(e)