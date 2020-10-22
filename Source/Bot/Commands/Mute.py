import datetime
from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.NoIntArgumentMuteCommandError import not_int_argument
from ..Strings.RU.Errors.NotAdminError import not_admin
from ..Strings.RU.Errors.MissingArgumentForCommandError import missing_argument
from ..Strings.RU.Errors.PointTargetError import point_target
from ..Strings.RU.Commands.MuteCommandUsed import mute_used
from ..Strings.RU.Commands.TaskDoneText import task_done
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved


async def mute_command(msg: types.Message):
    chat_id = msg.chat.id
    admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]

    try:
        sndr = msg.from_user
        target = msg.reply_to_message.from_user
        period_command_arg = msg.text.split(' ')[1]

        try:
            period_time = int(period_command_arg[:-1:])
        except ValueError:
            await msg.reply(
                not_int_argument,
                parse_mode = 'MarkdownV2'
            )

        if period_command_arg.endswith('h'):
            period = datetime.datetime.now() + datetime.timedelta(hours = period_time)
        if period_command_arg.endswith('m'):
            period = datetime.datetime.now() + datetime.timedelta(minutes = period_time)

        if sndr in admins:
            await walle.restrict_chat_member(
                chat_id,
                target.id,
                permissions = types.ChatPermissions (
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ),
                until_date = period
            )
            await walle.send_message(
                -1001471262276,
                mute_used.format(
                    returnNoneReserved(sndr.first_name),
                    sndr.url,
                    returnNoneReserved(target.first_name),
                    target.url,
                    returnNoneReserved('{}-{}-{} {}:{}:{}'.format(
                        str(msg.date.day),
                        str(msg.date.month),
                        str(msg.date.year),
                        str(msg.date.hour+4),
                        str(msg.date.minute),
                        str(msg.date.second)
                    )),
                    parse_mode = 'MarkdownV2'
                )
            )
            await msg.reply(task_done, parse_mode = 'MarkdownV2')
        else:
            await msg.reply(
                not_admin,
                parse_mode = 'MarkdownV2'
            )
    except IndexError:
        await msg.reply(
            missing_argument,
            parse_mode = 'MarkdownV2'
        )
    except AttributeError:
        await msg.reply(
            point_target,
            parse_mode = 'MarkdownV2'
        )
    except Exception as e:
        print(e)

