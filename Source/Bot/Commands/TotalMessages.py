from aiogram import types
from ..Bot import walle


async def get_total_messages(msg: types.Message):
    await msg.reply(
            'Общее кол-во сообщений: {}\nОбщее кол-во участников: {}'.format(
                str(msg.message_id),
                str(msg.chat.get_members_count())
            )
        )
