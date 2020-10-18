from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.NotAdminError import not_admin


async def pin_command(msg: types.Message):
    sndr = msg.from_user
    chat_id = msg.chat.id
    msg_id = msg.reply_to_message.message_id

    admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]

    try:
        if sndr in admins:
            await walle.pin_chat_message(
                chat_id,
                msg_id,
                False
            )
        else:
            await msg.delete()
            await msg.reply(
                not_admin,
                parse_mode = 'MarkdownV2'
            )
    except Exception as e:
        print(e)