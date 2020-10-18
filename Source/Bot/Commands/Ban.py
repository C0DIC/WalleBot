from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.NotAdminError import not_admin
from ..Strings.RU.Errors.PointTargetError import point_target
from ..Strings.RU.Commands.BanCommandUsedText import ban_used
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved

async def ban_command(msg: types.Message):
    chat_id = msg.chat.id
    admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]

    try:
        sndr = msg.from_user
        target = msg.reply_to_message.from_user

        if sndr in admins:
            await walle.kick_chat_member(
                chat_id,
                target.id
            )
            await walle.send_message(
                -1001471262276,
                ban_used.format(
                    returnNoneReserved(sndr.first_name),
                    sndr.url,
                    returnNoneReserved(target.first_name),
                    target.url,
                    returnNoneReserved(str(msg.date))
                )
            )
        else:
            await msg.reply(
                not_admin,
                parse_mode = 'MarkdownV2'
            )
    except  AttributeError:
        await msg.reply(
            point_target,
            parse_mode = 'MarkdownV2'
        )
    except Exception as e:
        print(e)