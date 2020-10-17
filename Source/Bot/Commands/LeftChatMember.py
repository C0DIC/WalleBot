from aiogram import types
from ..Bot import walle
from ..Strings.RU.Commands.LeftChatMemberText import user_left
from ..Strings.RU.Commands.RemovedChatMemberText import removed_user_text
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved


async def left_group_user(msg: types.Message):
    try:
        sndr = msg.from_user
        leftie = msg.left_chat_member

        if sndr.first_name == leftie.first_name:
            await walle.send_message(
                -1001471262276,
                user_left.format(
                    returnNoneReserved(leftie.first_name),
                    leftie.url,
                    returnNoneReserved(str(msg.date))
                ),
                parse_mode = 'MarkdownV2'
            )
        else:
            await walle.send_message(
                -1001471262276,
                removed_user_text.format(
                    returnNoneReserved(leftie.first_name),
                    leftie.url,
                    returnNoneReserved(sndr.first_name),
                    sndr.url,
                    returnNoneReserved(str(msg.date))
                ),
                parse_mode = 'MarkdownV2'
            )
        await msg.delete()
    except Exception as e:
        print(e)