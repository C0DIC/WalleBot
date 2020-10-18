from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.PointTargetError import point_target
from ..Strings.RU.Errors.NotAdminError import not_admin


async def unban_command(msg: types.Message):
    chat_id = msg.chat.id
    admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]
    
    try:
        sndr = msg.from_user
        target = msg.reply_to_message.from_user.id

        if sndr in admins:
            await walle.unban_chat_member(
                chat_id,
                target
            )
        else:
            await msg.reply(
                not_admin,
                parse_mode = 'MarkdownV2'
            )
    except AttributeError:
        await msg.reply(
            point_target,
            parse_mode = 'MarkdownV2'
        )