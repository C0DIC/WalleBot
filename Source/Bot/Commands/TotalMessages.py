from aiogram import types
from ..Bot import walle


async def get_total_messages(msg: types.Message):
    await msg.reply(
            'Общее кол-во сообщений: ' + str(msg.message_id)
        )
