from aiogram import types
from ..Bot import walle


async def stat_command(msg: types.Message):
    await msg.reply(
            'Общее кол-во сообщений: {}\nОбщее кол-во участников: {}'.format(
                str(msg.message_id),
                str(int(msg.chat.get_members_count()))
            )
        )
