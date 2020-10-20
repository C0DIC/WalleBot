from aiogram import types
from ..Bot import walle
from ..Strings.RU.Commands.StatCommandText import stat_text


async def stat_command(msg: types.Message):
    chat_id = msg.chat.id
    mems_count = await walle.get_chat_members_count(chat_id)

    await msg.reply(
            stat_text.format(
                str(msg.message_id),
                str(mems_count)
            )
        )
