from aiogram import types
from ..Bot import walle
from ..Strings.RU.Commands.LeftChatMemberText import user_left
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved


async def left_group_user(msg: types.Message):
    try:
        leftie = msg.left_chat_member

        await walle.send_message(
            -1001471262276,
            user_left.format(
                returnNoneReserved(leftie.first_name),
                leftie.url,
                returnNoneReserved(str(msg.date))
            )
        )
    except Exception as e:
        print(e)