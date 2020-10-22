from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.NotAdminError import not_admin
from ..Strings.RU.Errors.PointTargetError import point_target
from ..Strings.RU.Commands.BanCommandUsedText import ban_used
from ..Strings.RU.Commands.FormattedDateText import formatted_date
from ..Strings.RU.Commands.TaskDoneText import task_done
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
                target.id,
                until_date = 0
            )

            await walle.send_message(
                -1001471262276,
                ban_used.format(
                    returnNoneReserved(sndr.first_name),
                    sndr.url,
                    returnNoneReserved(target.first_name),
                    target.url,
                    returnNoneReserved(
                        formatted_date.format(
                            str(msg.date.day),
                            str(msg.date.month),
                            str(msg.date.year),
                            str(msg.date.hour+4),
                            str(msg.date.minute),
                            str(msg.date.second)
                        )
                    )
                ),
                parse_mode = 'MarkdownV2'
            )

            await msg.reply(task_done, parse_mode = 'MarkdownV2')
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