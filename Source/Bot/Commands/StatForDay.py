from aiogram import types
from ..Bot import walle


async def day_stat_command(msg: types.Message):
    try:
        msg_date = msg.date
        await msg.reply(msg_date)
    except Exception as e:
        print(e)